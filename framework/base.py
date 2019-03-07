from appium.webdriver.common.mobileby import By
from framework.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from appium.webdriver.common.touch_action import TouchAction
logger=Logger("Base").getlog()
class Base():
    def __init__(self,driver):
        self.driver=driver
    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("click the element")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed to click the elemetn with %s"%e)
    def back(self):
        self.driver.back()
        logger.info("back")
    def close(self):
        self.driver.close()
        logger.info("close")
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("clear text in input box before typing")
        except Exception as e:
            self.get_windows_img()
            logger.error("faild to clear in input box with %s"%e)
    def remove_app(self,app_package):
        self.driver.remove_app(app_package)
        logger.info("remove_app")
    def  is_app_install(self,app_package):
        bool=self.driver.is_app_install(app_package)
        logger.info("is_app_install")
        return bool

    def install_app(self,apk_path):
        self.driver.install_app(apk_path)
        logger.info("install_app")
    def quit(self):
        self.driver.quit()
        logger.info("quit")
    def reset(self):
        self.driver.reset()
        logger.info("result")
    def wait_activity(self):
        self.driver.wait_activity()
        logger.info("wait_activity")
    def implicitly_wait(self):
        self.driver.implicitly_wait()
        logger.info("implicitly_wait")
    def get_windows_img(self):
        file_path = os.path.dirname(os.path.abspath(".")) + "/screenshot/"
        rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        screen_name = file_path + rq + ".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("had take screenshot and save to folder:/scteenshots")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed to take screenshot! %s"%e)
    def get_text(self,*loc):
        el=self.find_element(*loc)
        try:
            text=el.text
            return text
        except Exception as e:
            self.get_windows_img()
            logger.error("failed get_text with %s"%e)



    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("successful find element")
        except Exception as e:
            self.get_windows_img()
            logger.error("faild find element with %s"%e)
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容：%s",text)
        except Exception as e:
            self.get_windows_img()
            logger.error("failed sendkeys with %s"%e)
    def swipe(self,start_x,starat_y,end_x,end_y,duration=10):
        self.driver.swipe(start_x,starat_y,end_x,end_y,duration)
        logger.info("swipe")
    def tap(self,*positions,duration=None):
        self.driver.tap(*positions)

    def flick(self,start_x, start_y, end_x, end_y):
        self.driver.flick(start_x,start_y,end_x,end_y)
    def zoom(self,element=None, precent=200, step=50):
        self.driver.zoom(element)
    def tijiao(self,*loc):
        el=self.find_element(*loc)
        try:
            el.submit()
            logger.info("tijiao")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed tijiao")
    def keyevent(self,num):
        self.driver.keyevent(num)
        logger.info("keysevent")
    def long_press(self,*loc):
        el=self.find_element(*loc)
        try:
            action1=TouchAction(self.driver)
            action1.long_press(el).wait(10).perform()
            logger.info("long_press")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed long_press with %s"%e)
    def move_to(self,*loc):
        el=self.find_element(*loc)
        try:
            action=TouchAction(self.driver)
            action.move_to(el).perform().release()
            logger.info("move_to")
        except Exception as e:
            self.get_windows_img()
            logger.error("failed move_to with %s"%e)
    def press_move_to(self,x1,y1,x2,y2):
        action1=TouchAction(self.driver)
        action1.press(x=x1,y=y1).wait(1000).move_to(x=x2,y=y2).release().perform()
        logger("press_move_to")
    def long_press_move(self,x1,y1,x2,y2):
        action=TouchAction(self.driver)
        action.long_press(x=x1,y=y1).wait(1000).move_to(x=x2,y=y2).release().perform()
        logger.info("long_press_move")
    def find_toast(self,message):
        try:
            message="//*[@text=\'{}\']".format(message)#Toast内容
            element=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(By.XPATH,message))
            logger.info("Get Toast:",element.text)
            return True
        except Exception as e:
            logger.error("Get Toast Error :",e)
            return False
