# coding=utf-8
__author__ = 'zhangteng'

import sys
from polyv.day_job import PolyvJob

if __name__ == "__main__":
    print(v for v in sys.argv)
    if sys.argv[1] == 'polyv':
        PolyvJob().do_job(sys.argv[2])
