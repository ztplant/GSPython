# coding=utf-8
__author__ = 'zhangteng'

from config import LOCAL
from datetime import datetime, timedelta
import json
from db import DB
import traceback
import threading

local_db = DB(LOCAL())
g_insert_sql = "insert into polyv_log values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

def insert_value(month):
    first_day = datetime.strptime("2017%s01" % month, '%Y%m%d')
    # for i in range(0,31):
    for day in ('20170211','20170115','20170816','20170628','20170629','20170630'):
        # day = (first_day + timedelta(days = i))
        try:
            # if day.month != int(month):
            #     break
            # day = day.strftime('%Y%m%d')
            f=open('/Users/zhangteng/Documents/gaosiedu_export/9/polyv/%s.txt' % day,'r')
            line = f.readline()
            json_line = json.loads(line)
            insert_value = []
            for e in json_line['data']:
                insert_value.append((e["playId"],e["userId"],e["videoId"],e["playDuration"],e["stayDuration"],e["currentTimes"],
                                     e["duration"],e["flowSize"],e["sessionId"],e["param1"],e["param2"],e["param3"],e["param4"],
                                     e["param5"],e["ipAddress"],e["country"],e["province"],e["city"],e["isp"],e["referer"],
                                     e["userAgent"],e["operatingSystem"],e["browser"],e["isMobile"],e["currentDay"],e["currentHour"],
                                     e["createdTime"],e["lastModified"]))
            local_db.execute(g_insert_sql, insert_value)
            print(day)
        except Exception as e:
            print(day, e)
            f.close()
        finally:
            f.close()

if __name__ == "__main__":
    # threads = []
    # t1 = threading.Thread(target=insert_value,args=('01',))
    # threads.append(t1)
    # t2 = threading.Thread(target=insert_value,args=('02',))
    # threads.append(t2)
    # t3 = threading.Thread(target=insert_value,args=('03',))
    # threads.append(t3)
    # t4 = threading.Thread(target=insert_value,args=('04',))
    # threads.append(t4)
    # t5 = threading.Thread(target=insert_value,args=('05',))
    # threads.append(t5)
    # t6 = threading.Thread(target=insert_value,args=('06',))
    # threads.append(t6)
    # t7 = threading.Thread(target=insert_value,args=('07',))
    # threads.append(t7)
    # t8 = threading.Thread(target=insert_value,args=('08',))
    # threads.append(t8)
    # t9 = threading.Thread(target=insert_value,args=('09',))
    # threads.append(t9)
    #
    # for t in threads:
    #     # t.setDaemon(True)
    #     t.start()
    #
    # for t in threads:
    #     t.join()
    #
    # print('all finished!')

    insert_value('01')