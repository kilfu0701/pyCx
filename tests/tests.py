import os
import sys

pyCx_module = os.path.abspath('../')
sys.path.insert(0, pyCx_module)

try:
    import pyCx
    print('pyCx version:', pyCx.__version__)
except:
    exit('Error! Cannot import pyCx package.')


from pyCx import Cx, CxQuery
from pyCx import CxFilter as CF
from pyCx import CxFilterOp as Op
from pyCx.helpers import date_range


class CxTest(object):
    def __init__(self):
        test_env = 'env.test.yaml'
        if not os.path.isfile(file_path):
            test_env = 'env.yaml'

        fp = os.path.abspath(test_env)
        cache_dir = os.path.abspath('.cache')

        self.cx = Cx(cx_config=CxConfig(fp), cache_dir=cache_dir)
        self.cq = self.cx.get_query()
        self.cq.apply_group('zuu')

    def get_users_traffic(self):
        csv_file = './sample_data/users.csv'
        dates = date_range('2018-10-01', '2018-11-01')
        return self.cq.get_traffic_by_users(csv_file, dates)

    def test_filters(self):
        pass


if __name__ == '__main__':
    ct = CxTest()

    ct.get_users_traffic()
    ct.test_filters()

