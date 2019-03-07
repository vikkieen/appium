from testsuites.base_testcase import BaseTestCase
from pageobjects.znbwl_addmemo import ZnbwlAddMemo
class AddMemoTest(BaseTestCase):
    def test_addmemo(self):
        addmemo=ZnbwlAddMemo(self.app.driver)
        addmemo.addmemo("style1","style2")