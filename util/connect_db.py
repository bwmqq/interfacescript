#-*-coding:utf-8-*-
import psycopg2

class Get_DBData:
	def __init__(self):
		pass

	# 连接数据库
	def get_db_connect(self, db_name, db_statement):
		# 通过connect方法创建数据库连接
		conn = psycopg2.connect(dbname=db_name, user="jeejio", password="jeejio", host="10.11.11.63", port="5432")
		# 创建cursor以访问数据库
		cur = conn.cursor()
		# 查询并打印(读取Retrieve)
		#print(cur.execute("select * from developer_info where create_user = 201909111001"))
		#执行sql语句
		cur.execute(db_statement)
		# rows = cur.fetchall()
		# print('--------------------------------------------------------------------------------------')
		# for row in rows:
		# 	print(str(row[0]) + str(row[1]))
		# 	print('--------------------------------------------------------------------------------------\n')
		#提交删除语句的操作
		conn.commit()
		cur.close()

		# 关闭连接
		conn.close()
