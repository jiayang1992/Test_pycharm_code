#coding=utf-8
from selenium import webdriver
# driver = webdriver.Firefox()
#调用浏览器
driver= webdriver.ChromeOptions()
executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ['webdriver.chrome.driver'] = executable_path
driver = webdriver.Chrome(executable_path,chrome_options=driver)
driver.get("http://www.baidu.com")
print ("浏览器最大化")
driver.maximize_window() #将浏览器最大化显示
driver.quit()
