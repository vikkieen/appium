import os
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver
apk_path=os.path.dirname(os.path.abspath("."))
desired_caps={}
desired_caps["platformName"]="Android"
desired_caps["platformVersion"]="4.4.2"
desired_caps["deviceName"]="127.0.0.1:62001"
desired_caps["sessionOverride"]=True

desired_caps["app"]=apk_path+"/app/znbwl.apk"
desired_caps["noReset"]=True

desired_caps["appPackage"]="com.pdswp.su.smartcalendar"
desired_caps["appActivity"]="com.pdswp.su.smartcalendar.WelcomeNote"
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.find_element_by_id("com.example.todolist:id/nameET")
driver.keyevent()
driver.swipe()

# driver.find_element_by_id("com.example.todolist:id/passwordET").send_keys("1")
# driver.find_element_by_id("com.example.todolist:id/loginBtn").click()
# driver.find_element_by_id("com.example.todolist:id/action_new").click()
# driver.find_element_by_id("com.example.todolist:id/toDoItemDetailET").send_keys("first")
# driver.find_element_by_id("com.example.todolist:id/saveBtn").click()
# driver.quit()
# driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
# driver.find_element_by_id("com.example.todolist:id/nameET").send_keys("1")
# driver.find_element_by_id("com.example.todolist:id/passwordET").send_keys("1")
# driver.find_element_by_id("com.example.todolist:id/loginBtn").click()
# action1=TouchAction(driver)
# el=driver.find_element_by_id("com.example.todolist:id/toDoItemDetailTv")
# action1.long_press(el).wait(5).perform()
# driver.find_elements_by_id("android:id/title")[1].click()
# driver.find_element_by_id("android:id/button1").click()
# driver.quit()