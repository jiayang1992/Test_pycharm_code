#coding utf-8
from selenium import webdriver
import time,os
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
#调用浏览器
driver= webdriver.ChromeOptions()
executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ['webdriver.chrome.driver'] = executable_path
driver = webdriver.Chrome(executable_path,chrome_options=driver)
driver.get("http://www.baidu.com")
print ("设置浏览器的宽高")
driver.set_window_size(480,800)
time.sleep(3)
driver.quit()
