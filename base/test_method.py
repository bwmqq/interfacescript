#coding=utf-8

import unittest
from demo import RunMain
import json
import HTMLTestRunner
from mock_demo import mock_test
class TestMethod (unittest.TestCase):

    def test_01(self):
        url = 'http://login.jeejio.com/user/users/accountLogin'
        data={
            'userKey':'17600253218',
            'userPasswd':'1234qwer'
        }
        headers = \
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
                "Content-Type": "application/json;charset=UTF-8"
            }
        run=RunMain(url, 'POST',headers, data)
        res=run.run_main( url, 'POST',headers, data).json()
        print(res)
        globals()['userID']=res['resultValue']['id']
        print(userID)
        self.assertEqual(res['statusCode'],200,'测试失败')
    def test_02(self):
        url = 'http://open.jeejio.com/developer/aptitude/getAptitudeUserByUserId'
        data={'createUser':userID}
        headers = \
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
                "Content-Type": "application/json;charset=UTF-8"
            }
        run = RunMain(url, 'POST', headers, data)
        res = run.run_main(url, 'POST', headers, data).json()
        print(res)
        self.assertEqual(res['statusCode'], 200, '测试失败')

    #@unittest.skip("这是模拟接口反馈，跳过该测试项")     #这句可以让下面的test_03不执行
    def test_03(self):
        url = 'http://open.jeejio.com/developer/aptitude/getAptitudeUserByUserId'
        data = {'createUser': userID}
        headers = \
                {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
                    "Content-Type": "application/json;charset=UTF-8"
                }
        run = RunMain(url, 'POST', headers, data)
        res=mock_test(run.run_main,data,url,'POST',{'statusCode': 200})   #模拟接口返回数据{'statusCode': 200}
        #res = run.run_main(url, 'POST', headers, data).json()
        print(res)
        self.assertEqual(res['statusCode'], 200, '测试失败')

if __name__ == '__main__':
    # unittest.main()
    filepath = "../report/htmlreport.html"
    fp = open(filepath,'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    suite.addTest(TestMethod('test_03'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title = 'this is a report')
    runner.run(suite)
    #unittest.TextTestRunner().run(suite)

