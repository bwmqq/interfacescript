import sys
sys.path.append('D:\IDE\Python37\Lib\site-packages')
import xlrd
from xlutils.copy import copy
import pandas as pd
from pandas import DataFrame
file_name = 'E:\InterfaceScript\openplatform\dataconfig\case1.xls'
data = xlrd.open_workbook(file_name)
sheets = data.sheet_names()
print(sheets)
alldata = DataFrame()
for i in range(len(sheets)):
    df = pd.read_excel(file_name, sheet_name=i, index=False, encoding='utf8')
    alldata = alldata.append(df)

print(alldata)


