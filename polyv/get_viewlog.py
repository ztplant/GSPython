# coding=utf-8
__author__ = 'zhangteng'

from config import Polyv
import hashlib
from datetime import datetime, timedelta
import urllib.request
import time
import threading

'''day=20160711&ptime=1468982782000&userid=e2e84a73837UagtQOq2A'''

g_url = "http://api.polyv.net/v2/data/%s/viewlog?day=%s&ptime=%s&sign=%s"

def get_content(month):
    first_day = datetime.strptime("2017%s01" % month, '%Y%m%d')
    for i in range(0,6):
        try:
            day = (first_day + timedelta(days = i))
            if day.month != int(month):
                break
            day = day.strftime('%Y%m%d')
            print(day)
            ptime = int(time.time())*1000
            pre_encry = "day=%s&ptime=%s&userid=%s" % (day, ptime, Polyv().userid + Polyv().secretkey)
            sign = hashlib.sha1(pre_encry.encode('UTF-8')).hexdigest().upper()
            url = g_url % (Polyv().userid, day, ptime, sign)
            data=urllib.request.urlopen(url).read().decode('UTF-8')
            f=open('/Users/zhangteng/Documents/gaosiedu_export/9/polyv/%s.txt' % day, 'w')
            f.write(data)
            f.close()
        except Exception as e:
            print(e)
            f.close()
        finally:
            f.close()




if __name__ == '__main__':
    threads = []
    t1 = threading.Thread(target=get_content,args=('09',))
    threads.append(t1)
    # t2 = threading.Thread(target=get_content,args=('02',))
    # threads.append(t2)
    # t3 = threading.Thread(target=get_content,args=('03',))
    # threads.append(t3)
    # t4 = threading.Thread(target=get_content,args=('04',))
    # threads.append(t4)
    # t5 = threading.Thread(target=get_content,args=('05',))
    # threads.append(t5)
    # t6 = threading.Thread(target=get_content,args=('06',))
    # threads.append(t6)
    # t7 = threading.Thread(target=get_content,args=('07',))
    # threads.append(t7)
    # t8 = threading.Thread(target=get_content,args=('08',))
    # threads.append(t8)

    for t in threads:
        # t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

    print('all finished!')