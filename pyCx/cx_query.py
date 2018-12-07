import os
import json
import pickle
import logging

import pandas as pd

from .cx_url import CxenseURL
from .cx_filter import CxFilter as CF
from .helpers import yesterday

class CxQuery(object):
    def __init__(self, cx, cache_dir='/tmp/.pyCx-cache', logger=logging):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug('initializing ...')

        self.cx = cx
        self._config = cx._config
        self._request_data = {}
        self._request_uri = ''
        self._cache_dir = cache_dir
        self._group = ''
        self._settings = {
            'retry': False,
            'retry_limit': 3,
        }
        self._retry_count = 0

        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    def get_traffic(self, user_token, dates=yesterday()):
        self.reset() \
            .uri(CxenseURL.TRAFFIC) \
            .add_filter(CF.User(user_token)) \
            .add_fields(['events', 'uniqueUsers']) \
            .add_history_fields(['events', 'uniqueUsers']) \
            .add_dates(dates)

        status, header, content = self.send()
        return content

    def uri(self, url_enum):
        self._request_uri = url_enum.value
        return self

    def apply_group(self, group):
        self._group = group
        return self

    def add_filter(self, fit):
        if 'filters' not in self._request_data:
            self._request_data['filters'] = []

        if fit['type'] == 'user':
            self.add_group(self._group)

        self._request_data['filters'].append(fit)
        return self

    def add_field(self, fd=''):
        return self.add_fields([fd])

    def add_fields(self, fds=['uniqueUsers']):
        self._request_data.setdefault('fields', [])
        self._request_data['fields'] += fds
        return self

    def add_history_field(self, fd=''):
        return self.add_history_fields([fd])

    def add_history_fields(self, fds=[]):
        self._request_data.setdefault('historyFields', [])
        self._request_data['historyFields'] += fds
        return self

    def add_group(self, group=''):
        return self.add_groups([group])

    def add_groups(self, groups=[]):
        self._request_data.setdefault('groups', [])
        self._request_data['groups'] += groups
        return self

    def add_dates(self, dates):
        self._request_data['start'], self._request_data['stop'] = dates[0:2]
        if dates[2] > 1:
            self._request_data['historyBuckets'] = dates[2]
        return self

    def reset(self):
        self._request_data = {
            'filters': [],
            'siteIds': [self._config['site_id']],
        }
        return self

    def send(self):
        self.logger.info('request {} {}'.format(self._request_uri, self._request_data))
        status, header, content = self.cx.execute(self._request_uri, json.dumps(self._request_data))

        if status != 200 and self._settings['retry']:
            if self._retry_count < self._settings['retry_limit']:
                self._retry_count += 1
                self.logger.warn('request failed... status={}, content={}'.format(status, content))
                self.logger.warn('retry... {}'.format(self._retry_count))
                return self.send()
            else:
                self.logger.error('retry limit reached, Stopped.')
                exit(1)

        self._retry_count = 0
        return status, header, content

    def dump(self):
        return self._request_uri, self._request_data

    def enable_retry(self, limit=3):
        self._settings['retry'] = True
        self._settings['retry_limit'] = limit
        return self

    def disable_retry(self):
        self._settings['retry'] = False
        return self

    """
    @csv_file -> 'users.csv'

    user_id,token
    1325,NOPCwHRQ2dzjZfdxhsjr
    579,f0gnmbksJ1VoNMV8PP18
    3,Js7PQzIrwvSvt4WvMs7X
    """
    # XXX: maybe this method should be move out of here.
    def get_traffic_by_users(self, csv_file, dates, info_columns=['user_id']):
        df_users = pd.read_csv(csv_file)
        data = {}
        pickle_file = '{}/users_traffic.pickle'.format(self._cache_dir)

        if os.path.isfile(pickle_file):
            with open(pickle_file, 'rb') as f:
                try:
                    data = pickle.load(f)
                except EOFError:
                    pass

        for idx, d in df_users.iterrows():
            token = d.token

            need_query = False
            if token not in data:
                need_query = True
                data[token] = {
                    'total': 0,
                    'traffic': {},
                    'fetched': [int(1e16), 0, 0],
                    'info': {},
                }

                for c in info_columns:
                    if c in df_users.columns:
                        data[token]['info'][c] = d[c]

            else:
                if dates[0] < data[token]['fetched'][0] or dates[1] > data[token]['fetched'][1]:
                    need_query = True

            if need_query:
                resp = self.get_traffic(d.token, dates)
                jd = json.loads(resp.decode('utf-8'))
                for idx, val in enumerate(jd['historyData']['events']):
                    ts = jd['history'][idx]
                    data[token]['traffic'][str(ts)] = val

                data[token]['total'] = jd['data']['events']
                data[token]['fetched'][0] = min(data[token]['fetched'][0], dates[0])
                data[token]['fetched'][1] = max(data[token]['fetched'][1], dates[1])
                data[token]['fetched'][2] = (data[token]['fetched'][1] - data[token]['fetched'][0]) // 86400

        # cache result
        with open(pickle_file, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return data
