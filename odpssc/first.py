# coding=utf-8
__author__ = 'zhangteng'

from odps import ODPS
from config import ODPSCONF


O = ODPS(ODPSCONF.key, ODPSCONF.sec, 'sync_data', endpoint='http://service.odps.aliyun.com/api')

f = open('odps_ddl_1208.txt','a')

i = 1
s = ''

for t in O.list_tables():
    print(i, t.name)
    s += "\n\n%s.\t%s\t%s\n" % (i, t.name, t.comment)
    s += t.schema.get_table_ddl().replace('table_name', t.name)
    i += 1
    if i % 5 == 0:
        f.write(s)
        s = ''

f.write(s)
f.close()