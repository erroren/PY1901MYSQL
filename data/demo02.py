import pymysql
try:
    conn = pymysql.Connect(host="localhost", port=3306,
                           user="root", password="123456", database="goods", charset="utf8")
    cur1 = conn.cursor()
    count = cur1.execute("insert into user(id,name,addr) values(0,'user6','addr6')")
    print(count)
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
finally:
    cur1.close()
    conn.close()
