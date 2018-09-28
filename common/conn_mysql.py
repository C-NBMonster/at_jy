#coding:utf-8
"""
pymysql.Connect()参数说明
host(str):      MySQL服务器地址
port(int):      MySQL服务器端口号
user(str):      用户名
passwd(str):    密码
db(str):        数据库名称
charset(str):   连接编码

connection对象支持的方法
cursor()        使用该连接创建并返回游标
commit()        提交当前事务
rollback()      回滚当前事务
close()         关闭连接

cursor对象支持的方法
execute(op)     执行一个数据库的查询命令
fetchone()      取得结果集的下一行
fetchmany(size) 获取结果集的下几行
fetchall()      获取结果集中的所有行
rowcount()      返回数据条数或影响行数
close()         关闭游标对象

"""

import pymysql.cursors

class C_mysql():

    # 连接数据库
    def connect_DB(self, host, port, user, pwd, dbName, charset):
        global connect
        connect = pymysql.Connect(
            host = host, #'10.50.31.85',
            port = port, #3306,
            user = user, #'credit_rw@10.50.31.%',
            passwd = pwd, #'Cdrw$201805',
            db = dbName, #'credit',
            charset = charset #'utf-8'
        )
        # 获取游标
        global cursor
        cursor = connect.cursor()

    # 插入数据
    def Insert(self, sql, data=''):
        """
        插入数据
        :param sql: SQL语句
        :param data: 插入字段的值，有顺序限制。设定空值是为了解放sql，不受固定形式限制
        :usage:
        sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', '%.2f' )"
        data = ('雷军', '13512345678', 10000)
        :return:
        """
        if data == '':
            cursor.execute(sql)
        else:
            cursor.execute(sql % data)
        connect.commit()
        print('成功插入', cursor.rowcount, '条数据')

    # 修改数据
    def Update(self, sql, data=''):
        """
        插入数据
        :param sql: SQL语句
        :param data: 插入字段的值，根据表字段顺序填写。设定空值是为了解放sql，不受固定形式限制
        :usage:
        sql = "UPDATE trade SET saving = '%.2f' WHERE account = '%s' "
        data = (8888, '13512345678')
        :return:
        """
        if data == '':
            cursor.execute(sql)
        else:
            cursor.execute(sql % data)
        connect.commit()
        print('成功修改', cursor.rowcount, '条数据')

    # 查询数据
    def Search(self, sql, data=''):
        """
        插入数据
        :param sql: SQL语句
        :param data: 插入字段的值，根据表字段顺序填写。设定空值是为了解放sql，不受固定形式限制
        :usage:
        sql = "SELECT name,saving FROM trade WHERE account = '%s' "
        data = ('13512345678')
        :return:
        """
        if data == '':
            cursor.execute(sql)
        else:
            cursor.execute(sql % data)
        for row in cursor.fetchall():
            print("Name:%s\tSaving:%.2f" % row)
        print('共查找出:', cursor.rowcount, '条数据')

    # 删除数据
    def delete(self, sql, data=''):
        """
        插入数据
        :param sql: SQL语句
        :param data: 插入字段的值，根据表字段顺序填写。设定空值是为了解放sql，不受固定形式限制
        :usage:
        sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
        data = ('13512345678', 1)
        :return:
        """
        if data == '':
            cursor.execute(sql)
        else:
            cursor.execute(sql % data)
        connect.commit()
        print('成功删除', cursor.rowcount, '条数据')

    # 事务处理,这个以后在优化，一般处理存储过程吧。20180928
    def tansection(self):
        sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
        sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
        sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "

        try:
            cursor.execute(sql_1)  # 储蓄增加1000
            cursor.execute(sql_2)  # 支出增加1000
            cursor.execute(sql_3)  # 收入增加2000
        except Exception as e:
            connect.rollback()  # 事务回滚
            print('事务处理失败', e)
        else:
            connect.commit()  # 事务提交
            print('事务处理成功', cursor.rowcount)

    # 关闭连接
    def close(self):
        cursor.close()
        connect.close()
