# 1.导入模块
import pymysql

# 2.创捷连接实例
con = pymysql.Connect(host="localhost", user="root", password="123456", database="goods")
# 3创建游标对象
cursor = con.cursor()
# 4通过游标操作数据库

cursor.execute("select * from user")
# 5获取游标中数据
result = cursor.fetchone()
print(result)
result = cursor.fetchmany(2)
print(result)
result = cursor.fetchall()
print(result)
cursor.scroll(-1)
result = cursor.fetchone()
print(result)
# 6释放连接实例
cursor.close()
con.close()
