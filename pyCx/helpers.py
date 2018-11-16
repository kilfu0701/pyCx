import os
import time
from datetime import datetime, timedelta

os.environ['TZ'] = 'Asia/Tokyo'
time.tzset()

def yesterday():
    today = datetime.today()
    t_date = datetime(today.year, today.month, today.day)
    y_date = t_date - timedelta(days=1)
    return [int(y_date.timestamp()), int(t_date.timestamp()), 1]

"""
@param start String '2018-10-01'
@param end   String '2018-10-02'
@return      Object [int, int, int(historyBuckets)]
"""
def date_range(start, end):
    s_date = datetime.strptime(start, '%Y-%m-%d')
    e_date = datetime.strptime(end, '%Y-%m-%d')
    s_date_ts = int(s_date.timestamp())
    e_date_ts = int(e_date.timestamp())
    intervals = (e_date_ts - s_date_ts) // 86400
    return [s_date_ts, e_date_ts, intervals]

def dates_to_array(dates, formats='%m/%d'):
    dt = []
    ds = dates[0]
    while ds < dates[1]:
        dt.append(datetime.fromtimestamp(ds).strftime(formats))
        ds += 86400

    return dt
