#coding=utf-8
from selenium import webdriver
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox()
#调用浏览器
driver= webdriver.ChromeOptions()
executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ['webdriver.chrome.driver'] = executable_path
driver = webdriver.Chrome(executable_path,chrome_options=driver)
file_path='file:///' + os.path.abspath('层级定位.html')
driver.get(file_path)

#点击Link1弹出下拉菜单
driver.find_element_by_link_text('Link1').click()

#在父原件下找到link为Action的元素
menu = driver.find_element_by_id('dropdown1').find_element_by_link_text('Another action ')

#鼠标移动到子元素上
ActionChains(driver).move_to_element(menu).perform()
time.sleep(2)
driver.quit()