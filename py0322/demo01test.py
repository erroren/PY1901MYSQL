import py0322.demo01 as d1
# 查询一条
result = d1.PyMysqlHelp().select_one("select * from user where id=%s", (2,))
print(result)
# 查询全部
result = d1.PyMysqlHelp().select_all("select * from user where id > %s", (2,))
print(result)
# 查询多条
result = d1.PyMysqlHelp().select_number("select * from user where id > %s", (2,), 2)
print(result)
# 插入信息
# res = d1.PyMysqlHelp().update("insert into user values(0,%s,%s)", ("nn", "aa"))
# print(res)
# # 修改信息
# res = d1.PyMysqlHelp().update("update user set name = %s where name=%s", ("newnn", "nn"))
# print(res)
# 删除
# res = d1.PyMysqlHelp().update("delete from user where name=%s", ("newnn",))
# print(res)