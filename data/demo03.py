import pymysql
conn = pymysql.Connect(host="localhost", user="root", password="123456", database="goods")
cur = conn.cursor()
count = cur.execute("update user set name='user5' where name='用户5'")
print(count)
conn.commit()
cur.close()
conn.close()
