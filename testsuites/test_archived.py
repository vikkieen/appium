from testsuites.base_testcase import BaseTestCase
from pageobjects.znbwl_archived import ZnbwlArchived
class ArchivedTest(BaseTestCase):
    def test_archived(self):
        arch=ZnbwlArchived(self.app.driver)
        arch.archived()
        try:
            self.assertEqual(arch.duanyan,arch.name,msg=arch.duanyan)
            print("归档成功")
        except Exception as e:
            print("失败 with %s"%e)