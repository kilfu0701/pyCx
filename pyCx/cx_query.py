import os
import json
import pickle

import pandas as pd

from .cx_url import CxenseURL
from .cx_filter import CxFilter as CF
from .helpers import yesterday
from .decorators import uri, with_base_parameters

class CxQuery(object):
    def __init__(self, cx, cache_dir='/tmp/.pyCx-cache'):
        self.cx = cx
        self._config = cx._config
        self._request_data = {}
        self._request_uri = ''
        self._cache_dir = cache_dir
        self._group = ''

        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)

    @uri(CxenseURL.TRAFFIC)
    @with_base_parameters
    def get_traffic(self, user_token, dates=yesterday()):
        self.add_filter(CF.User(user_token)) \
            .add_fields(['events', 'uniqueUsers']) \
            .add_dates(dates)

        status, header, content = self._exec()
        return content

    def apply_group(self, group):
        self._group = group
        return self

    def add_filter(self, fit):
        if fit['type'] == 'user':
            fit['group'] = self._group

        self._request_data['filters'].append(fit)
        return self

    def add_fields(self, fds=['uniqueUsers']):
        self._request_data['fields'] = fds
        return self

    def add_dates(self, dates):
        self._request_data['start'], self._request_data['stop'], self._request_data['historyBuckets'] = dates

    def reset(self):
        self._request_data = {
            'filters': [],
        }
        return self

    def _exec(self):
        return self.cx.execute(self._request_uri, json.dumps(self._request_data))

    """
    @csv_file -> 'users.csv'

    user_id,token
    1325,NOPCwHRQ2dzjZfdxhsjr
    579,f0gnmbksJ1VoNMV8PP18
    3,Js7PQzIrwvSvt4WvMs7X
    """
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
                    'fetched': [10**16, 0, 0],
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
                data[token]['fetched'][2] = (data[token]['fetched'][1] - data[token]['fetched'][0]) / 86400

        # cache result
        with open(pickle_file, 'wb') as handle:
            pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

        return data
