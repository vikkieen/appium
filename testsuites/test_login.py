from testsuites.base_testcase import BaseTestCase
from pageobjects.znbwl_login import ZnbwlLogin
from ddt import data, ddt, unpack
from framework.util import Util
import unittest
import os
testdata=Util.get_execl(os.path.dirname(os.path.abspath("."))+"/data/user.xlsx","Sheet1")
@ddt
class LoginTest(BaseTestCase):
    @data(*testdata)
    def test_login(self,data):
        login=ZnbwlLogin(self.app.driver)
        print(data["email"],data['password'])
        login.login(data["email"],data["password"])
        try:
            self.assertEqual(login.duanyan,"智能备忘录",msg=login.duanyan)
            print("成功登陆")
        except Exception as e:
            print("登录失败 with %s"%e)

if __name__=="__main__":
    unittest.main()