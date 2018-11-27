import os

from pyCx import CX, CxQuery
from pyCx import CxFilter as CF
from pyCx import CxFilterOp as Op
from pyCx.helpers import date_range



class CxTest(object):
    def __init__(self):
        fp = os.path.abspath('env.yaml')
        cache_dir = os.path.abspath('.cache')

        self.cx = Cx(cx_config=CxConfig(fp), cache_dir=cache_dir)
        self.cq = self.cx.get_query()
        self.cq.apply_group('zuu')


    def get_users_traffic(self):
        csv_file = '.test_users.csv'
        dates = date_range('2018-10-01', '2018-11-01')
        return self.cq.get_traffic_by_users(csv_file, dates)


    def test_filters(self):
        self.cq

        pass


if __name__ == '__main__':
    ct = CxTest()

    ct.get_users_traffic()
    ct.test_filters()





