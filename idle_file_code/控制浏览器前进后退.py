#coding utf-8
from selenium import webdriver
import time,os
# driver = webdriver.Firefox()
#调用浏览器
driver= webdriver.ChromeOptions()
executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ['webdriver.chrome.driver'] = executable_path
driver = webdriver.Chrome(executable_path,chrome_options=driver)
#访问百度页面
first_url=("http://www.baidu.com")
print ("now access %s" %(first_url))
driver.get(first_url)
time.sleep(2)

#访问新页面
second_url=("http://news.baidu.com")
print ("now access %s" %(second_url))
driver.get(second_url)
time.sleep(2)

#返回（后退）到百度首页
print ("back to %s" %(first_url))
driver.back()
time.sleep(2)

#前进到新页面
print ("forward to %s" %(second_url))
driver.forward()
time.sleep(2)

driver.quit()

