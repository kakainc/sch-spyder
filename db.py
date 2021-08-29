# --->
# Created by liumeiyu on 2020/3/18.
# '_'

import pymysql


conn = pymysql.connect(host='localhost', user='root', password='123456', port=3306, charset='utf8', db='spyder')
cursor = conn.cursor()
cursor.execute("select version()")
data = cursor.fetchone()


def sql_data(csr, sql):
    csr.execute(sql)


if __name__ == '__main__':
    print(" Database Version:%s" % data)
    # mq = './sqls/creat_table.sql'
    # sql_data(cursor, mq)
