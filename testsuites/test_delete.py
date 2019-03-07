from testsuites.base_testcase import BaseTestCase
from pageobjects.znbwl_delete import ZnbwlDelete
class DeleteTest(BaseTestCase):
    def test_delete(self):
        delete=ZnbwlDelete(self.app.driver)
        delete.delete()