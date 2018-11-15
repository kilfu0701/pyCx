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

def set_recursion_limit(param):
    def wrapper(f):
        sys.setrecursionlimit(param)
        return f

    return wrapper
