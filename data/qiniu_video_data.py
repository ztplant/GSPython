# coding=utf-8
__author__ = 'zhangteng'
#-*-coding:utf-8-*-
import os
import re
from datetime import datetime
from gzip import GzipFile
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/bi')
insert_sql = 'insert into video_log_copy(`datetime`,url) values (%s, %s)'
done_list = []

def parse_url_time(filedir):
    filelist = os.listdir(filedir)
    for path in filelist:
        filepath = filedir + '/' + path
        if not os.path.isfile(filepath) or filepath in done_list or not filepath.endswith('.gz'):
            continue
        print("--"+filepath)
        _parse_url_time(filepath)

def _parse_url_time(filepath):
    row_sql = []
    data_num = 1
    with GzipFile(filepath, 'r') as fi:
        lines = fi.readlines()
        for line in lines:
            line = str(line)
            time_arr = re.findall(r'\[(.*?)\+', line, flags=0)
            if len(time_arr) != 1 :
                continue
            time_str = time_arr[0].strip()
            ti = datetime.strptime(time_str, '%d/%b/%Y:%H:%M:%S')

            url_arr = re.findall(r'http[s]?.*?\"', line,flags=0)
            if len(url_arr) == 0:
                continue
            url = url_arr[0].rstrip('HTTPS"').strip()
            if '.mp4' in url:
                row_sql.append((ti, url))
                data_num += 1
                if data_num >= 1000:
                    do_insert(row_sql)
                    row_sql = []
                    data_num = 1
        do_insert(row_sql)

def do_insert(row_sql):
    print(len(row_sql))
    if len(row_sql) > 0:
        try:
            engine.execute(insert_sql, row_sql)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    parse_url_time('/v2/')