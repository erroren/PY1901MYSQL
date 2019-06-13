import pymysql

class PyMysqlHelp():
    def __init__(self, _database="goods", _host="localhost", _port=3306, _user="root",
                 _password="123456", _charset="utf8"):
        self.conn = None
        self.cur = None
        try:
            self.conn = pymysql.Connect(host=_host, user=_user, password=_password,
                                        database=_database, port=_port, charset=_charset)
            self.cur = self.conn.cursor()
        except Exception as e:
            print(e)

    def select_one(self, sql, args=None):
        try:
            self.cur.execute(sql, args)
            return self.cur.fetchone()
        except Exception as e:
            print(e)
        finally:
            self._close()

    def select_number(self, sql, args=None, n=0):
        try:
            self.cur.execute(sql, args)
            return self.cur.fetchmany(n)
        except Exception as e:
            print(e)
        finally:
            self._close()

    def select_all(self, sql, args=None):
        try:
            self.cur.execute(sql, args)
            return self.cur.fetchall()
        except Exception as e:
            print(e)
        finally:
            self._close()

    def update(self, sql, args=None):
        try:
            res = self.cur.execute(sql, args)
            self.conn.commit()
            return res
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            self._close()

    def _close(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
