import http.client as httplib
import os
import sys
import hmac
import json
import hashlib
import datetime
import urllib.parse as urlparse
import logging

import yaml

from .cx_query import CxQuery
from .cx_config import get_config, CxConfig
from .cx_url import CxenseURL
from .decorators import with_env

class Cx(object):

    @with_env('home')
    def __init__(self, cx_config=None, cache_dir='/tmp/.pyCx-cache', log_level=logging.INFO):
        self._init_logger(log_level)
        self.logger.debug('initializing ...')

        if isinstance(cx_config, CxConfig):
            self._config = cx_config.value()

        # init CxQuery
        self._query = CxQuery(self, cache_dir=cache_dir, logger=logging)

    def get_query(self):
        return self._query

    def get_date(self, connection):
        try:
            connection.request("GET", "/public/date")
            return json.load(connection.getresponse())['date']
        except:
            pass

        return datetime.datetime.utcnow().isoformat() + "Z"

    def execute(self, path, content):
        if path.startswith('http'):
            url = urlparse.urlparse(path)
        else:
            url = urlparse.urlparse(urlparse.urljoin(self._config['apiserver'], path))

        connection = (httplib.HTTPConnection if url.scheme == 'http' else httplib.HTTPSConnection)(url.netloc)
        try:
            dt = self.get_date(connection)
            signature = hmac.new(self._config['secret'].encode('utf-8'), dt.encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
            headers = {"X-cXense-Authentication": "username=%s date=%s hmac-sha256-hex=%s" % (self._config['username'], dt, signature)}
            headers["Content-Type"] = "application/json; charset=utf-8"
            connection.request("GET" if content is None else "POST", url.path + ("?" + url.query if url.query else ""), content, headers)
            response = connection.getresponse()
            status, header, content = response.status, response.getheader('Content-Type', ''), response.read()
            if status != 200:
                raise Exception(status, str(content.decode('utf-8')))

            return status, header, content
        finally:
            connection.close()

    def _init_logger(self, log_level):
        # init logger
        logging.basicConfig(
            level=log_level,
            format='%(levelname)-8s %(asctime)s %(name)-12s %(message)s',
            datefmt='%Y/%m/%d %H:%M:%S'
        )
        logging.StreamHandler(sys.stdout)
        logging.addLevelName(logging.INFO, "\033[1;36m%s\033[1;0m   " % logging.getLevelName(logging.INFO))
        logging.addLevelName(logging.DEBUG, "\033[1;35m%s\033[1;0m  " % logging.getLevelName(logging.DEBUG))
        logging.addLevelName(logging.WARNING, "\033[1;33m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
        logging.addLevelName(logging.ERROR, "\033[1;41m%s\033[1;0m  " % logging.getLevelName(logging.ERROR))
        self.logger = logging.getLogger(self.__class__.__name__)

