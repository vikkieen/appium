from framework.base import Base
from appium.webdriver.common.mobileby import By
import time
class ZnbwlSearch(Base):
    button1 = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 搜索按钮图标
    search_button=(By.ID,"com.pdswp.su.smartcalendar:id/toolbar_search")
    search_text=(By.ID,"android:id/search_src_text")
    aim=(By.ID,"com.pdswp.su.smartcalendar:id/note_title")
    asser = (By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")
    def search(self,title):
        self.click(*self.search_button)
        self.sendkeys(title,*self.search_text)
        self.keyevent("66")

        self.click(*self.aim)
        self.duanyan =self.get_text(*self.asser)
        self.click(*self.button1)
        time.sleep(2)