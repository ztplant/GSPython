# coding=utf-8
__author__ = 'zhangteng'

from db import DB
from config import HMySQL
import time

conn = DB(HMySQL())

day_l = []

for day in day_l:
    begin = time.time()
    update_sql = "UPDATE dw_student_behavior SET event_time = unix_timestamp(event_time_fstr) * 1000 WHERE day='%s'" % day
    result = conn.execute(update_sql)
    end = time.time()
    print(day, "rows ", result.rowcount, "cost", end-begin)
