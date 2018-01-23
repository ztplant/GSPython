# coding=utf-8
__author__ = 'zhangteng'

from odps import ODPS
from config import ODPSCONF
from datetime import datetime


O = ODPS(ODPSCONF.key, ODPSCONF.sec, 'sync_data', endpoint='http://service.odps.aliyun.com/api')


# get name of partition
def get_partition_name():
    for t in O.list_tables():
        for p in t.schema.partitions:
            if 'week' in p.name:
                print(t.name)


def get_last_modify_time():
    for t in O.list_tables():
        print(t.name, t.last_modified_time.strftime('%Y%m%d'), t.last_modified_time.strftime('%Y%m%d') >= '20171213')


if __name__ == '__main__':
    get_last_modify_time()