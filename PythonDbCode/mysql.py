#!/usr/bin/python3
import pymysql


class MySql:
    def __init__(self, host, port, user, pass_wd, db_name, charset="utf8"):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=pass_wd,
            db=db_name,
            charset=charset
        )

    def __del__(self):
        self.conn.close()

    def run_sql_value(self, sql_str, data):
        cursor = self.conn.cursor()
        cursor.execute(sql_str)
        for tmp_tup in cursor.fetchall():
            tmp_list = []
            for val in tmp_tup:
                tmp_list.append(val)
            data.append(tmp_list)
        cursor.close()

    def run_sql(self, sql_str):
        cursor = self.conn.cursor()
        cursor.execute(sql_str)
        self.conn.commit()
        cursor.close()


if __name__ == "__main__":
    print("please import the module!")
