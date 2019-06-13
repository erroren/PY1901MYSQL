from py0322.demo01 import PyMysqlHelp
from hashlib import sha1
a = 3
while True:
    d1 = PyMysqlHelp()
    name = []
    sname = input("请输入用户名:")
    sql1 = "select name from account"
    res = d1.select_all(sql1)
    for i in range(0, len(res)):
        name.append(res[i][0])
    if sname not in name:
        print("账户不存在,请重新输入")
        continue
    pwd = input("请输入密码:")
    s1 = sha1()
    s1.update(pwd.encode("utf8"))
    spwd = s1.hexdigest()
    sql2 = "select password from account where name=%s"
    d2 = PyMysqlHelp()
    res = d2.select_one(sql2, (sname,))[0]
    if res == spwd:
        print("登录成功")
        break
    else:
        a = a-1
        print("密码错误,还有{}次机会".format(a))
        if a == 0:
            print("次数用完了")
            break
        continue

