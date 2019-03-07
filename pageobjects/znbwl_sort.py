from framework.base import Base
from appium.webdriver.common.mobileby import By
import time
class ZnbwlSort(Base):
    aim=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")
    paixu=(By.ID,"com.pdswp.su.smartcalendar:id/menu_sort")
    serial=(1030,200)
    seria2=(1030,330)
    seria3=(1030,470)
    seria4=(1030,600)
    sure=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_ok")
    def sort(self):
        self.long_press(*self.aim)
        self.click(*self.paixu)
        time.sleep(2)
        self.swipe(1030,160,1030,300,0)
        # self.move_to_bylocal(1000,200,1000,300)
        self.click(*self.sure)
        time.sleep(2)
