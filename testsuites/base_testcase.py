import unittest
import os
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
from framework.app_engine import AppEngine
import warnings
class BaseTestCase(unittest.TestCase):
    app=AppEngine()
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.app.open_app()
        # apk_path = os.path.dirname(os.path.abspath("."))
        # desired_caps = {}
        # desired_caps["platformName"] = "Android"
        # desired_caps["platformVersion"] = "4.4.2"
        # desired_caps["deviceName"] = "127.0.0.1:62001"
        # desired_caps["sessionOverride"] = True
        #
        # desired_caps["app"] = apk_path + "/app/znbwl.apk"
        # desired_caps["noReset"] = True
        #
        # desired_caps["appPackage"] = "com.pdswp.su.smartcalendar"
        # desired_caps["appActivity"] = "com.pdswp.su.smartcalendar.WelcomeNote"
        # self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


    def tearDown(self):
        self.app.close_app()
        # self.driver.quit()

