import http.client as httplib
import os
import hmac
import json
import hashlib
import datetime
import urllib.parse as urlparse

import yaml

from .cx_query import CxQuery
from .cx_config import get_config
from .cx_url import CxenseURL
from .decorators import with_env

class Cx(object):

    @with_env('home')
    def __init__(self, cx_config=None, cache_dir='/tmp/.pyCx-cache'):
        if cx_config is not None:
            self._config = cx_config.value()

        # init CxQuery
        self._query = CxQuery(self, cache_dir=cache_dir)

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
