from enum import Enum

class CxFilter(object):
    @staticmethod
    def User(user_token, group='cx'):
        # e.g.
        #   group='thk'
        #   user_token='RandomStringHere'
        return {
            'type': 'user',
            'group': group,
            'item': user_token,
        }

    @staticmethod
    def UserFirstParty(group, items=[]):
        # e.g.
        #   group='thk-salary'
        #   items=['5M', '10M']
        return {
            'type': 'user-external',
            'group': group,
            'items': items,
        }

    @staticmethod
    def CustomParameter(group, items=[]):
        # e.g.
        #   group='status'
        #   items=['ProMember']
        return {
            'type': 'custom',
            'group': group,
            'items': items,
        }

class CxFilterOp(Enum):
    And = 'and'
    Or  = 'or'
