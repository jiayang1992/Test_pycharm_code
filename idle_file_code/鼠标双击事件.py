#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import os,time

#设置浏览器
option= webdriver.ChromeOptions()
executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
os.environ['webdriver.chrome.driver'] = executable_path
driver = webdriver.Chrome(executable_path,chrome_options=option)

#获取浏览器路径，注意是webdriver.chrome获取链接所以使用driver调用地址
driver.get("http://101.201.41.228:6800/manage/user/home")
driver.find_element_by_id("userNameCopy").send_keys("admin")
time.sleep(10)
driver.find_element_by_name("password").send_keys("666666")
driver.implicitly_wait(10)
driver.find_element_by_name("isSavePwd").click()
driver.find_element_by_id("btnLogin").click()
