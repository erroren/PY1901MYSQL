import pymysql
conn = pymysql.Connect(host="localhost", user="root", password="123456", database="test")
cur = conn.cursor()
# file1 = './data/q1.jpg'
# cur.execute("insert into message(img) values(%s)", (file1,))
# conn.commit()
cur.execute("select img from message")
# a = cur.fetchone()[0]
# print(a)
# print(type(cur.fetchone()))
a = cur.fetchone()[0]
print(a)
file1 = open(file=a, mode="rb")
file2 = open(file="./data/p2.jpg", mode="wb")
file2.write(file1.read())
file2.close()
file1.close()
cur.close()
conn.close()
