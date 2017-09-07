# coding=utf-8
__author__ = 'zhangteng'

from db import DB
from config import Polyv, BiMySQL
import hashlib
import urllib.request
import time
import json


class PolyvJob:

    def __init__(self):
        self.g_url = "http://api.polyv.net/v2/data/%s/viewlog?day=%s&ptime=%s&sign=%s"
        self.g_insert_sql = "insert into polyv_log values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.db = DB(BiMySQL())

    def do_job(self,day):
        print(day)
        try:
            self.db.execute("TRUNCATE TABLE polyv_log")
            ptime = int(time.time())*1000
            pre_encry = "day=%s&ptime=%s&userid=%s" % (day, ptime, Polyv.userid + Polyv.secretkey)
            sign = hashlib.sha1(pre_encry.encode('UTF-8')).hexdigest().upper()
            url = self.g_url % (Polyv.userid, day, ptime, sign)
            data = urllib.request.urlopen(url).read().decode('UTF-8')
            print(day, url, 'got data')
            json_line = json.loads(data)
            insert_value = []
            for e in json_line['data']:
                insert_value.append((e["playId"],e["userId"],e["videoId"],e["playDuration"],e["stayDuration"],e["currentTimes"],
                                     e["duration"],e["flowSize"],e["sessionId"],e["param1"],e["param2"],e["param3"],e["param4"],
                                     e["param5"],e["ipAddress"],e["country"],e["province"],e["city"],e["isp"],e["referer"],
                                     e["userAgent"],e["operatingSystem"],e["browser"],e["isMobile"],e["currentDay"].replace('-',''),
                                     e["currentHour"],e["createdTime"],e["lastModified"]))
            self.db.execute(self.g_insert_sql, insert_value)
            print(day, 'finish')
        except Exception as e:
            print(day, e)
        finally:
            self.db.close()

