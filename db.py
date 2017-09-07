__author__ = 'zhangteng'


from sqlalchemy import create_engine


class DB:

    ENGINE_STR_TEMP = 'mysql://%s:%s@%s:%s/%s?charset=utf8'

    def __init__(self, source):
        db_engine = create_engine(self.ENGINE_STR_TEMP % (source.user, source.password, source.host, source.port, source.database), echo=False, pool_recycle=3600)
        self.db_conn = db_engine.connect()

    def execute(self, sql, params=None):
        if params is None:
            return self.db_conn.execute(sql)
        else:
            return self.db_conn.execute(sql, params)

    def get_sql_list(self, sql):
        return [v for v in self.visit(self.execute(sql))]

    def visit(self, results):
        for r in results:
            yield dict(zip(results.keys(), r))

    def get_sql_dict(self, sql):
        results = self.execute(sql)
        if results.rowcount > 0:
            return dict(zip(results.keys(),results.fetchone()))
        else:
            return {}
    
    def get_list(self, sql):
        return [v[0] for v in list(self.execute(sql))]

    def close(self):
        self.db_conn.close()