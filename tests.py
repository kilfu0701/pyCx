import os

from pyCx import CX, CxQuery
from pyCx.helpers import date_range

if __name__ == '__main__':
    fp = os.path.abspath('env.yaml')
    cache_dir = os.path.abspath('.cache')

    cx = Cx(cx_config=CxConfig(fp), cache_dir=cache_dir)
    cq = cx.get_query()
    cq.apply_group('zuu')

    dates = date_range('2018-10-01', '2018-11-01')
    traffic_data = cq.get_traffic_by_users('.test_users.csv', dates)
    print(traffic_data)
