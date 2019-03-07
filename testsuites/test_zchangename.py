from testsuites.base_testcase import BaseTestCase
from pageobjects.znbwl_changename import ZnbwlChangeName
from pageobjects.znbwl_login import ZnbwlLogin
class ChangeNameTest(BaseTestCase):
    def test_changename(self):
        # login=ZnbwlLogin(self.app.driver)
        # login.login("1233211234567@qq.com","123456789")
        changename=ZnbwlChangeName(self.app.driver)
        changename.changename("wowowo")
        try:
            self.assertEqual(changename.duanyan,"wowowo",msg=changename.duanyan)
            print("更改名字成功")
        except Exception as e:
            print("更改名字失败 with %s"%e)