# coding=utf-8
__author__ = 'zhangteng'

from .db_config import OdpsConn
import openpyxl
import datetime


class Exporter:

    def export(self, table):
        data_list = self.__get_data(table=table)
        self.__write_excel(data_list=data_list)

    def __write_excel(self, data_list):
        wb = openpyxl.Workbook()
        sheet = wb.active
        for i in range(0, len(data_list)):
            for j in range(0, len(data_list[i])):
                sheet.cell(row=i + 1, column=j + 1, value=str(data_list[i][j]))
        wb.save('/Users/zhangteng/Desktop/%s.xlsx' % datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

    def __get_data(self, table):
        with OdpsConn('sync_data') as conn:
            result = conn.execute_sql("select * from %s limit 10" % table)
            return result
