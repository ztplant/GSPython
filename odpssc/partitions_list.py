# coding=utf-8
__author__ = 'zhangteng'

from odps import ODPS
from config import ODPSCONF


O = ODPS(ODPSCONF.key, ODPSCONF.sec, 'sync_data', endpoint='http://service.odps.aliyun.com/api')


t = O.get_table('dw_dt_class_lesson')
p = t.get_partition('day=20171112')
print(p.size)
print(p.PartitionMeta)