import pymysql
conn = pymysql.Connect(host="localhost", port=3306,
                       user="root", password="123456", database="goods", charset="utf8")
# cur = conn.cursor(pymysql.cursors.DictCursor)
# cur.execute("select  * from user")
# print(cur.fetchone()['name'])
# print(cur.fetchall())
cur = conn.cursor()
res = cur.executemany("insert into user values(%s,%s,%s)", [(0, "tom", "d1"), (0, "tom1", "d2")])
print(res)
conn.commit()
cur.close()
conn.close()
