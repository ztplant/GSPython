# coding=utf-8
__author__ = 'zhangteng'

'''
odps 建表语句转mysql
'''

for line in open('ddl.txt'):
    line = line.strip()
    if line.find("CREATE TABLE") >= 0 :
        # 首行
        print(line.replace("tran_","o_"))
    elif line == ")":
        print(") ENGINE=InnoDB DEFAULT CHARSET=utf8;")
    else :
        '''
          `ins_id` int(11) NOT NULL DEFAULT '0' COMMENT '机构ID',
          `ins_name` varchar(40) DEFAULT NULL COMMENT '机构名称',
          `renew_num` int(11) DEFAULT NULL COMMENT '续费账号数',
          `expired_num` int(11) DEFAULT NULL COMMENT '过期账号数',
          `result` varchar(20) DEFAULT NULL COMMENT '续费情况',
          `rate` double(11,2) DEFAULT '0.00' COMMENT '占比',
        '''
        print("    ", end='')
        if line.find("BIGINT") >= 0:
            print(line.replace("BIGINT", "int(11) NOT NULL DEFAULT '0'"))
        elif line.find("STRING") >= 0:
            print(line.replace("STRING", "varchar(255) DEFAULT ''"))
        elif line.find("DOUBLE") >= 0:
            print(line.replace("DOUBLE", "double(11,2) DEFAULT '0.00'"))