#coding:utf-8
import sys
sys.path.append("C:/Users/DELL/Desktop/data/interfacescript2")
import operator
import json
import time
from base.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependdentData
from util.send_email import SendEmail
#from util.operation_header import OperationHeader
from util.operation_json import OperetionJson
from util.operation_excel import OperationExcel
from util.connect_db import Get_DBData

class RunTest:
	def __init__(self):
		self.run_method = RunMethod()
		self.com_util = CommonUtil()
		self.send_mail = SendEmail()
		self.oper_db = Get_DBData()

	#执行测试用例的主函数
	def go_on_run(self):
		oe = OperationExcel()
		res = None
		pass_count = []
		fail_count = []

		sheet_num = oe.get_sheets_number()
		for j in range(0, sheet_num):
			oe.sheet_no = j
			data=GetData(j)
			rows_count = data.get_case_lines()
			for i in range(1,rows_count):
				is_run = data.get_is_run(i)
				db_name = data.get_db_name(i)
				db_statement = data.get_db_statement(i)
				if db_name != None:
					# print(db_name)
					self.oper_db.get_db_connect(db_name, db_statement)
					time.sleep(3)
				if is_run:
					url = data.get_request_url(i)
					method = data.get_request_method(i)
					request_data = data.get_request_data(i)
					#expect = self.data.get_expcet_data_for_mysql(i)
					expect=str(int(data.get_expect_data(i)))
					header =data.is_header(i)
					depend_case =data.is_depend(i)
					if depend_case != None:
						depend_num = depend_case.count(",")
						if depend_num ==0:
							#获取依赖数据
							depend_sheet_no = int(depend_case.split(":")[0])
							depend_caseid = depend_case.split(":")[1]
							depend_data = data.get_depend_key(i)
							depend = DependdentData(depend_sheet_no, depend_caseid)
							depend_response_data = str(depend.get_data_for_key(depend_data))
							depend_key = data.get_depend_field(i)
							request_data = json.loads(request_data)
							#将依赖key的value赋给请求数据的key
							request_data[depend_key] = depend_response_data
							request_data = json.dumps(request_data)
						else:
							for n in range(0,depend_num):
								depend_case1 = str(depend_case.split(",")[n])
								depend_sheet_no1 = int(depend_case1.split(":")[n])
								depend_caseid1 = depend_case1.split(":")[n]
								#获取当前测试用例的依赖数据
								depend_data = data.get_depend_key(i)
								depend_data1= str(depend_data.split(",")[n])
								#实例化DependdentData类
								depend1 = DependdentData(depend_sheet_no1,depend_caseid1)
								#获取依赖key的value
								depend_response_data1 = str(depend1.get_data_for_key(depend_data1))
			 					#获取依赖的请求数据,对应excel表中依赖的请求数据字段
								depend_key = data.get_depend_field(i)
								depend_key1 = str(depend_key.split(",")[n])
								# 把请求数据从json格式转换成字典
								request_data = json.loads(request_data)
								#将依赖key的value赋给请求数据的key
								request_data[depend_key1] = depend_response_data
								#把字典转换成json格式
								request_data = json.dumps(request_data)
					if header == 'write':
						res = self.run_method.run_main(method,url,request_data)
						op_header = OperationHeader(res)
						op_header.write_cookie()

					elif header == 'yes':
						headers = \
							{
							"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
							"Content-Type": "application/json;charset=UTF-8"
							}
						res = self.run_method.run_main(method,url,request_data,headers)
					else:
						res = self.run_method.run_main(method,url,request_data)
					if self.com_util.is_contain(expect,str(res["success"])):
						data.write_result(i,'pass')
						data.write_return_result(i,str(res))
						pass_count.append(i)
					else:
						data.write_result(i,'fail')
						data.write_return_result(i, str(res))
						fail_count.append(i)
					time.sleep(2)
			# self.send_mail.send_main(pass_count,fail_count)

	#将执行判断封装
	#def get_cookie_run(self,header):


if __name__ == '__main__':
	runTest = RunTest()
	runTest.go_on_run()











