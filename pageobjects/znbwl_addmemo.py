from framework.base import Base
from appium.webdriver.common.mobileby import By
import time
class ZnbwlAddMemo(Base):
    button1 = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 搜索按钮图标
    add_button=(By.ID,"com.pdswp.su.smartcalendar:id/menuAdd")
    content_input=(By.ID,"com.pdswp.su.smartcalendar:id/add_input_content")
    sure=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    add_memo=(By.ID,"com.pdswp.su.smartcalendar:id/design_menu_item_text")
    def addmemo(self,content1,content2):
        self.click(*self.add_button)
        self.sendkeys(content1,*self.content_input)
        self.click(*self.sure)
        self.click(*self.button1)
        self.click(*self.add_memo)
        self.sendkeys(content2,*self.content_input)
        time.sleep(3)
