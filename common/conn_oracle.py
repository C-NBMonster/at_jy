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

import cx_Oracle

class C_oracle():
    # 连接数据库
    def __init__(self):
        user=u'dafy_sales'
        passwd = u'Ju$2017'
        print(cx_Oracle.clientversion())
        host = 'idcdbtest.dafycredit.com'
        #host = "10.11.11.71"
        port = 1521
        dbname='testdb'
        #dsn = cx_Oracle.makedsn(host, port, dbname)
        self.conn = cx_Oracle.connect("dafy_sales","Ju$2017","idcdbtest.dafycredit.com:1521/DBTEST01")
        self.cursor = self.conn.cursor()

    # 查询数据

    def oracle_Search(self, sql):
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            print("Name:%s\tSaving:%.2f" % row)
        print('共查找出', self.cursor.rowcount, '条数据')
        return result

    def __del__(self):
        # 关闭连接
        self.cursor.close()
        self.conn.close()





""""
# 获取游标
cursor = conn.cursor()


# 插入数据
sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
data = ('雷军', '13512345678', 10000)
cursor.execute(sql % data)
conn.commit()
print('成功插入', cursor.rowcount, '条数据')

# 修改数据
sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
data = (8888, '13512345678')
cursor.execute(sql % data)
conn.commit()
print('成功修改', cursor.rowcount, '条数据')



# 删除数据
sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
data = ('13512345678', 1)
cursor.execute(sql % data)
conn.commit()
print('成功删除', cursor.rowcount, '条数据')

# 事务处理
sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "

try:
    cursor.execute(sql_1)  # 储蓄增加1000
    cursor.execute(sql_2)  # 支出增加1000
    cursor.execute(sql_3)  # 收入增加2000
except Exception as e:
    conn.rollback()  # 事务回滚
    print('事务处理失败', e)
else:
    conn.commit()  # 事务提交
    print('事务处理成功', cursor.rowcount)
"""
# # 关闭连接
#     cursor.close()
#     conn.close()
