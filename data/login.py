from data import pymysqlhelper as sql

# result = sql.MySqlHelper().select_one("select * from user where name = %s", ("tom",))
# print(result)
# res = sql.MySqlHelper.update("insert into user(id,name,addr) values(0,%s,%s)",("aa", "bb"))
# print(res)

# result = sql.MySqlHelper().select_many("select * from user")
# print(result)
# result = sql.MySqlHelper.update("insert into user (id,name,addr) values(0,%s,%s)",("aa", "bb"))
# print(result)

# sql.MySqlHelper().update("update user set name = %s ")