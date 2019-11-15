#coding:utf-8
import requests
import json
class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		if header !=None:	
			res = requests.post(url=url,data=data,headers=header).json()
		else:
			res = requests.post(url=url,data=data).json()
		return res

	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:	
			res = requests.get(url=url,data=data,headers=header,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		return res.json()

	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'Post' or 'post':
			res = self.post_main(url,data.encode('utf-8'),header)
		else:
			res = self.get_main(url,data.encode('utf-8'),header)
		return res
		#return json.dumps(res,ensure_ascii=False)
		#return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
