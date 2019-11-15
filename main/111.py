#-*-coding:utf-8-*-
import psycopg2


#通过connect方法创建数据库连接
conn = psycopg2.connect(dbname="user_dev", user="jeejio",password="Jeejio@2018", host="10.10.10.20", port="20004")

# 创建cursor以访问数据库
cur = conn.cursor()
#查询并打印(读取Retrieve)
cur.execute("select * from um_users where user_phone= '17600253218'")
rows = cur.fetchall()
print('--------------------------------------------------------------------------------------')
for row in rows:
    print(  str(row[0])  + str(row[1]))
print('--------------------------------------------------------------------------------------\n')
# 关闭连接
conn.close()