from testsuites.base_testcase import BaseTestCase
from pageobjects.znbwl_sort import ZnbwlSort
class SortTest(BaseTestCase):
    def test_sort(self):
        sort=ZnbwlSort(self.app.driver)
        sort.sort()