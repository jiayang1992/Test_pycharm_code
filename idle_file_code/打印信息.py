#coding=utf-8
from selenium import webdriver
import time,os
# driver = webdriver.Firefox()
#调用浏览器
driver= webdriver.ChromeOptions()
executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ['webdriver.chrome.driver'] = executable_path
driver = webdriver.Chrome(executable_path,chrome_options=driver)
driver.get("http://edu.yunlansoft.com/admin/login.action")

driver.find_element_by_name("user.name").clear()
driver.find_element_by_name("user.name").send_keys("admin")

driver.find_element_by_name("user.passwd").clear()
driver.find_element_by_name("user.passwd").send_keys("123456")
driver.find_element_by_name("sm1").click()

#获得title打印
now_url = driver.current_url
print(now_url)

#当前url和预期url做比较
if now_url == "http://edu.yunlansoft.com/frame/main.action":
    print("url ok")
else:
    print("url on")
    time.sleep(2)
driver.quit()





