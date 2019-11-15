import requests
import json


class RunMain:

    def __init__(self, url, method,headers=None, data=None):
        self.res = self.run_main(url,method,headers,data)

    def send_get(self, url,headers, data):
        res = requests.get(url=url, headers=headers,data=data)
        return res

    def send_post(self, url,headers,data):
        res = requests.post(url=url,headers=headers, data=json.dumps(data))
        return res

    def run_main(self, url, method,headers=None, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, headers,data)
        else:
            res = self.send_post(url,headers,data)
        return res


if __name__ == '__main__':
    #url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html'
    #data = {
    #    'cart': '11'
    #}
    url = 'http://login.jeejio.com/user/users/accountLogin'
    data = {
        'userKey': '17600253218',
        'userPasswd': '123'
    }
    headers = \
        {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "Content-Type": "application/json;charset=UTF-8"
        }
    run = RunMain(url, 'POST',headers, data)
    print(run.res.json())
# print run.run_main(url,'GET',data)
