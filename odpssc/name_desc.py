# coding=utf-8
__author__ = 'zhangteng'


from odps import ODPS
from config import ODPSCONF

O = ODPS(ODPSCONF.key, ODPSCONF.sec, 'sync_data', endpoint='http://service.odps.aliyun.com/api')

for t in O.list_tables():
    print(t.name + "\t" + t.comment)