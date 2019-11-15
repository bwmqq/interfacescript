#coding:utf-8
import sys
import json
sys.path.append('C:/Users/DELL/Desktop/data/interfacescript2')
from util.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
class DependdentData:
	def __init__(self,sheet_id,case_id):
		self.case_id = case_id
		self.sheet_id = sheet_id
		self.opera_excel = OperationExcel(self.sheet_id)
		self.data = GetData(self.sheet_id)

	#根据case_id去获取该case的整行数据
	def get_case_line_data(self):
		rows_data = self.opera_excel.get_rows_data(self.case_id)
		return rows_data

	#执行依赖的case，得到接口返回结果
	def run_dependent(self):
		run_method = RunMethod()
		#获取依赖case的行号
		row_num  = self.opera_excel.get_row_num(self.case_id)
		#获取依赖case的请求数据
		request_data = self.data.get_request_data(row_num)
		header = self.data.is_header(row_num)
		headers =\
		 	{
		 	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
		 	"Content-Type": "application/json;charset=UTF-8"
		     }
		method = self.data.get_request_method(row_num)
		url = self.data.get_request_url(row_num)
		res = run_method.run_main(method,url,request_data,headers)
		return res

	#根据依赖的key获取key的value
	def get_data_for_key(self,depend_data):
		#获取依赖的请求数据
		json_expr = parse(depend_data)
		#获取依赖case的行号
		row_num  = self.opera_excel.get_row_num(self.case_id)
        #获取依赖case的接口返回结果
		response_data1 = self.data.get_result_res(row_num)
		response_data = eval(response_data1)
		print(depend_data)
		depend_data = eval(str(depend_data))
		return depend_data
		#return ([match.value for match in json_expr.find(response_data1)][0])
		# return ([match.value for match in json_expr.find(response_data["resultValue"])][0])
		# key_value =response_data['resultValue'][depend_data]
		# print(key_value)
		# res_data = response_data.txt.decode('utf-8')
		# res_data = json.loads(response_data.text)
		# print(res_data)


if __name__ == '__main__':
	pass



