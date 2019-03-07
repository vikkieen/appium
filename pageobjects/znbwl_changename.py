from framework.base import Base
from appium.webdriver.common.mobileby import By
class ZnbwlChangeName(Base):
    button1 = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 搜索按钮图标
    login_button = (By.ID, "com.pdswp.su.smartcalendar:id/username")  # 点击进入登录按钮
    name_box=(By.ID,"com.pdswp.su.smartcalendar:id/title")
    name_text=(By.ID,"com.pdswp.su.smartcalendar:id/username")
    sure=(By.ID,"com.pdswp.su.smartcalendar:id/quick_add")
    def changename(self,name):
        self.click(*self.button1)
        self.click(*self.login_button)
        self.click(*self.name_box)
        self.sendkeys(name,*self.name_text)
        self.click(*self.sure)
        self.click(*self.button1)
        self.click(*self.button1)
        self.duanyan=self.get_text(*self.login_button)