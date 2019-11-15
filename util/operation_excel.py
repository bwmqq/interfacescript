#coding:UTF-8
import sys
sys.path.append('C:/Users/DELL/AppData/Local/Programs/Python/Python37/Lib/site-packages')
import xlrd
from xlutils.copy import copy
class OperationExcel:
	data= None

	def __init__(self,sheet_no = None):
		self.file_name = "C:/Users/DELL/Desktop/data/interfacescript2/dataconfig/market.xls"
		if sheet_no:
			self.sheet_no = sheet_no
		else:
			self.sheet_no = 0
		self.data = self.get_data()

	#获取excel表sheet的个数
	def get_sheets_number(self):
		data = xlrd.open_workbook(self.file_name)
		sheets_number = len(data.sheet_names())
		return sheets_number

	#获取sheet的内容
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_no]
		return tables

	#获取单元格的行数
	def get_lines(self):
		tables = self.get_data()
		return tables.nrows

	#获取某一个单元格的内容
	def get_cell_value(self,row,col):
		content = self.get_data().cell_value(row, col)
		return content

	#写入数据
	def write_value(self,row,col,value):
		'''
		写入excel数据
		row,col,value
		'''
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		sheet_data = write_data.get_sheet(self.sheet_no)
		sheet_data.write(row,col,value)
		write_data.save(self.file_name)

	#根据对应的caseid 找到对应行的内容
	def get_rows_data(self,case_id):
		row_num = self.get_row_num(case_id)
		rows_data = self.get_row_values(row_num)
		return rows_data

	#根据对应的caseid找到对应的行号
	def get_row_num(self,case_id):
		num = 0
		cols_data = self.get_cols_data()
		for col_data in cols_data:
			if case_id in col_data:
				return num
			num = num+1


	#根据行号，找到该行的内容
	def get_row_values(self,row):
		tables = self.data
		row_data = tables.row_values(row)
		return row_data

	#获取某一列的内容
	def get_cols_data(self,col=None):
		sheet = self.get_data()
		if col!= None:
			cols = sheet.col_values(col_id)
		else:
			cols = sheet.col_values(0)
		return cols



if __name__ == '__main__':
	opers = OperationExcel(0)
	print(opers.get_cell_value(2, 9))