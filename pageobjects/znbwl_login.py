from framework.base import Base
from appium.webdriver.common.mobileby import By
import time
class ZnbwlLogin(Base):
    button1 = (By.ID, "com.pdswp.su.smartcalendar:id/ab_icon2")  # 搜索按钮图标
    login_button = (By.ID, "com.pdswp.su.smartcalendar:id/username")  # 点击进入登录按钮
    email=(By.ID,"com.pdswp.su.smartcalendar:id/email")#登录账号
    pwd=(By.ID,"com.pdswp.su.smartcalendar:id/password")#登录密码
    submit=(By.ID,"com.pdswp.su.smartcalendar:id/login")#登录按钮
    exit=(By.ID,"com.pdswp.su.smartcalendar:id/exit")#退出当前账号
    asser=(By.ID,"com.pdswp.su.smartcalendar:id/index_ab_title")
    def login(self,email,pwd):
        self.click(*self.button1)
        self.click(*self.login_button)
        self.sendkeys(email,*self.email)
        self.sendkeys(pwd,*self.pwd)
        self.click(*self.submit)
        self.duanyan=self.get_text(*self.asser)
        print(self.duanyan)
        self.click(*self.button1)
        self.click(*self.login_button)
        self.click(*self.exit)