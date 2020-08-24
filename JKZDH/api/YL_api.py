# coding = utf-8
import requests,json
from conf.user_conf import *
session=requests.session()
class CMs_api(object):
    def __init__(self):
        pass
    def login(self):
        rep=session.post(url=login_url,data=login_data)
        # print(rep.text)
        return rep.json()['token']
    def query(self):
        rep=session.post(url=query_url,data=query_data)
        print(rep.text)
        return rep.json()
    def mengan(self,content):
        #post验证
        mengan_data = json.dumps({'content': content})
        headers = {
            'content-type': 'application/json;charset=utf-8'
        }
        res = requests.post(url=mengan_url,data=mengan_data,headers=headers)
        return res.json()

if __name__=='__main__':
        c=CMs_api()
        c.login()
        c.query()
        c.mengan('mingan')