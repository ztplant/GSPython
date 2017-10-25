# coding=utf-8
__author__ = 'zhangteng'

from config import Polyv
import hashlib
from datetime import datetime, timedelta
import urllib.request
import time
import sys

'''day=20160711&ptime=1468982782000&userid=e2e84a73837UagtQOq2A'''

g_url = "http://api.polyv.net/v2/data/%s/viewlog?day=%s&ptime=%s&sign=%s&vid=%s"

def create_url(day, vid):
    ptime = int(time.time())*1000
    pre_encry = "day=%s&ptime=%s&userid=%s" % (day, ptime, Polyv().userid + Polyv().secretkey)
    sign = hashlib.sha1(pre_encry.encode('UTF-8')).hexdigest().upper()
    url = g_url % (Polyv().userid, day, ptime, sign, vid)
    # data = urllib.request.urlopen(url).read().decode('UTF-8')
    print(url)


if __name__ == '__main__':

    create_url('20171012','01b768ec8c55f14f0bd1f48e9efc3b59_0')
    print('all finished!')