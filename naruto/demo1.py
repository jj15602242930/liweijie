import pymysql


def get_conn():
    db = pymysql.connect("localhost", "root", "root", "test", charset='utf8')
    return db


# 验证登录的方法
class com():
    def chark(username, password):
        db = get_conn()
        cur = db.cursor()
        sql = "select * from user where user='%s'" % username
        cur.execute(sql)
        rs = cur.fetchall()
        print(rs != ())
        if rs != ():
            if password in rs[0]:
                return True
            else:
                return False
            return False

# 注册时查看是否已存在账号
    def chark_user(user):
        db = get_conn()

        cur = db.cursor()

        sql3 = 'select * from user WHERE user = "%s"' % user

        cur.execute(sql3)

        rs = cur.fetchall()
        if rs != ():
            if user in rs[0]:
                print("用户名密码已存在")
                return True
            else:
                print('注册成功')
                return False
            return False

# 注册成功插入数据库
    def insers(user,pawd):
        print(666)
        db = get_conn()
        cur = db.cursor()
        sql2 = 'INSERT into user set user= "%s" , pass= "%s" ' % (user, pawd)
        print(555)
        cur.execute(sql2)
        db.commit()
        print('注册成功')
