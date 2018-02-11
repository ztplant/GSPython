# coding=utf-8
__author__ = 'zhangteng'

import sys
from polyv.day_job import PolyvJob
from odpssc.exporter import Exporter

if __name__ == "__main__":
    if sys.argv[1] == 'polyv':
        PolyvJob().do_job(day=sys.argv[2])
    if sys.argv[1] == 'export':
        Exporter().export(table=sys.argv[2])