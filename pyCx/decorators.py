import sys
from functools import wraps

from .cx_config import get_config

def with_env(param):
    def wrapper(f):
        @wraps(f)
        def decorated(self, *args, **kwargs):
            username, secret, apiserver = get_config(param)
            _config = {
                'username': username,
                'secret': secret,
                'apiserver': apiserver,
                'siteId': 0,
            }
            self.__dict__.update({'_config': _config})
            return f(self, *args, **kwargs)
        return decorated
    return wrapper


def uri(param):
    def wrapper(f):
        @wraps(f)
        def decorated(self, *args, **kwargs):
            self.__dict__.update({'_request_uri': param.value})
            return f(self, *args, **kwargs)
        return decorated
    return wrapper


def with_base_parameters(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        self._request_data = {}
        self.__dict__.update({
            '_request_data': {
                'siteIds': [self._config['site_id']],
            }
        })
        return func(self, *args, **kwargs)
    return wrapper


def set_recursion_limit(param):
    def wrapper(f):
        sys.setrecursionlimit(param)
        return f

    return wrapper
