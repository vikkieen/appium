from framework.base import Base
from appium.webdriver.common.mobileby import By
import time
class ZnbwlArchived(Base):
    aim = (By.ID, "com.pdswp.su.smartcalendar:id/note_title")
    button1 = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 搜索按钮图标
    guidang=(By.ID,"com.pdswp.su.smartcalendar:id/menu_archive")
    arch_memu=(By.NAME,"归档")
    title=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")
    recover=(By.NAME,"恢复")
    sear=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")
    def archived(self):
        self.name=self.get_text(*self.sear)
        self.long_press(*self.aim)
        self.click(*self.guidang)
        self.click(*self.button1)
        self.click(*self.arch_memu)
        time.sleep(2)
        self.duanyan = self.get_text(*self.sear)
        self.swipe(820,180,500,180,1000)
        self.click(*self.recover)
        time.sleep(2)

