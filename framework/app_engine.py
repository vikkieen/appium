import yaml
from appium import webdriver
import os
from framework.logger import Logger
class AppEngine():
    def open_app(self):
        # path=os.path.abspath(os.path.abspath("."))+"/config/config.yaml"
        with open(os.path.dirname(os.path.abspath("."))+"/config/config.yaml","r",encoding="utf-8") as file:
            data=yaml.load(file)
        desired_caps = {}
        desired_caps["platformName"] = data["platformName"]
        desired_caps["platformVersion"] =data["platformVersion"]
        desired_caps["deviceName"] = data["deviceName"]
        desired_caps["sessionOverride"] = data["sessionOverride"]
        app_path=os.path.dirname(os.path.abspath("."))+"/app/znbwl.apk"
        desired_caps["app"] = app_path
        desired_caps["noReset"] = data["noReset"]

        desired_caps["appPackage"] = data["appPackage"]
        desired_caps["appActivity"] = data["appActivity"]
        self.driver = webdriver.Remote("http://"+str(data['ip'])+":"+str(data["port"])+"/wd/hub",desired_caps)
        self.driver.implicitly_wait(5)
    def close_app(self):
        self.driver.quit()
if __name__=="__main__":
    app=AppEngine()
    app.open_app()
    app.close_app()