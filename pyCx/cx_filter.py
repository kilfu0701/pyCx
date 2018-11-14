


class CxFilter(object):

    @staticmethod
    def User(user_token):
        return {
            'type': 'user',
            'group': '',
            'item': user_token,
        }



