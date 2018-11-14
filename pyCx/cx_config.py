import os
import yaml

"""
[env.yaml]

default:
  site_id: your_id
  username: your_name
  secret: your_key
  apiserver: https://api.cxense.com

zuu:
  site_id: your_id
  username: your_name
  secret: your_key
  apiserver: https://api.cxense.com
"""

class CxConfig(object):
    def __init__(self, env_file_path):
        with open(env_file_path, 'r') as stream:
            self.env = yaml.load(stream)

    def value(self, key='default'):
        return self.env[key]


def get_config(env_key):
    username = secret = apiserver = None

    # Locate and autoload configuration from ~/.cxrc
    rc = os.path.join(os.path.expanduser('~'), '.cxrc')
    if os.path.exists(rc):
        for line in open(rc):
            fields = line.split()
            if fields[0] == 'authentication' and len(fields) == 3:
                username = fields[1]
                secret = fields[2]
            elif fields[0] == 'apiserver' and len(fields) == 2:
                apiserver = fields[1]

    return username, secret, apiserver
