# -*- coding:utf-8 -*-
# __author__ = majing

from functools import wraps
from odps import ODPS
from config import ODPSCONF


def catch_exception(func):
    @wraps(func)
    def _catch_exception(*args, **kwargs):
        try:
            rest = func(*args, **kwargs)
            return rest
        except Exception as exc:
            raise ValueError(exc.message)
    return _catch_exception


class OdpsConn(object):
    """
    odps 连接
    """
    def __init__(self, project):
        self.access_id = ODPSCONF.key
        self.access_key = ODPSCONF.sec
        self.project = project

        self.odps = None

    def __enter__(self):
        try:
            self.odps = ODPS(self.access_id, self.access_key, self.project)
        except Exception as exc:
            raise ValueError(exc.message)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self

    def get_table_count_and_names(self):
        """
        获取一个项目下的table的数量和table的名字
        :return:
        """
        tables = self.odps.list_tables()
        names = [table.name for table in tables]
        count = len(names)
        return count, names

    def get_table_schema(self, tname):
        """
        获取表字段
        :return: 
        """
        table = self.odps.get_table(tname)
        _sa = table.schema
        _columns = _sa.columns
        schema = [item.name for item in _columns]
        return schema

    def execute_sql(self, sql):
        rest = []
        with self.odps.execute_sql(sql).open_reader() as reader:
            for record in reader:
                rest.append(record.values)
        return rest

    def get_table_last_update_time(self, tname):
        t = self.odps.get_table(tname)
        last_update_time = t.last_modified_time if t else None
        return last_update_time

    def count_table(self, table):
        sql = 'select count(1) from %s' % table
        with self.odps.execute_sql(sql).open_reader() as reader:
            return reader[0].values[0]