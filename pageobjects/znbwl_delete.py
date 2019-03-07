from framework.base import Base
from appium.webdriver.common.mobileby import By
class ZnbwlDelete(Base):
    button1 = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 搜索按钮图标
    aim=(By.ID, "com.pdswp.su.smartcalendar:id/note_title")
    recycle=(By.NAME,"回收站")
    delete_button=(By.ID,"com.pdswp.su.smartcalendar:id/menu_delete")
    clear=(By.ID,"com.pdswp.su.smartcalendar:id/button")
    sure=(By.NAME,"确认")
    postion=[900,1080]
    def delete(self):
        self.long_press(*self.aim)
        self.click(*self.delete_button)
        self.click(*self.button1)
        self.click(*self.recycle)
        self.click(*self.clear)
        # self.click(*self.sure)
        self.tap([(900,1080)],0)
