from framework.base import Base
from appium.webdriver.common.mobileby import By
class ZnbwlRegiste(Base):
    button1=(By.ID,"com.pdswp.su.smartcalendar:id/ab_icon2")#搜索按钮图标
    login_button=(By.ID,"com.pdswp.su.smartcalendar:id/username")#点击进入登录按钮
    zhuce=(By.ID,"com.pdswp.su.smartcalendar:id/register")#点击进入注册按钮
    name=(By.ID,"com.pdswp.su.smartcalendar:id/username")#昵称
    email=(By.ID,"com.pdswp.su.smartcalendar:id/email")#邮箱
    pwd=(By.ID,"com.pdswp.su.smartcalendar:id/password")#密码
    reguser=(By.ID,"com.pdswp.su.smartcalendar:id/reguser")#登录按钮
    asser = (By.ID, "com.pdswp.su.smartcalendar:id/index_ab_title")
    def registe(self,name,email,pwd):
        self.click(*self.button1)
        self.click(*self.login_button)
        self.click(*self.zhuce)
        self.sendkeys(name,*self.name)
        self.sendkeys(email,*self.email)
        self.sendkeys(pwd,*self.pwd)
        self.click(*self.reguser)
        self.duanyan=self.get_text(*self.asser)

