from testsuites.base_testcase import BaseTestCase
from pageobjects.znbwl_search import ZnbwlSearch


class SearchTest(BaseTestCase):
    def test_search(self):
        search=ZnbwlSearch(self.app.driver)
        search.search("style1")
        try:
            self.assertEqual(search.duanyan,"查看备忘",msg=search.duanyan)
            print("查看成功")
        except Exception as e:
            print("查看失败 with %s"%e)