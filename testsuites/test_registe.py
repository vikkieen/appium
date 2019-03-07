from testsuites.base_testcase import BaseTestCase
from pageobjects.znbwl_registe import ZnbwlRegiste
class RegisteTest(BaseTestCase):
    def test_registe(self):
        try:
            registe=ZnbwlRegiste(self.app.driver)
            registe.registe("vikkieen","123321123451@qq.com","123456789")

            self.assertEqual(registe.duanyan,"智能备忘录",msg=registe.duanyan)
            print("注册成功")
        except Exception as e:
            print("注册失败 with %s"%e)
