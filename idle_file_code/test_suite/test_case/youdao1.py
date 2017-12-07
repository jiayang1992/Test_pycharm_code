#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re,os
class Youdao(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=option)
        self.base_url = "http://www.youdao.com"
        self.verificationErrors = []
        self.accept_next_alert = True
#有道搜索用例
    def test_youdao_search(self):
        u"""有道搜索"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("translateContent").send_keys(u"虫师")
        driver.find_element_by_link_text("翻译").click()
        time.sleep(2)
    def tearDown(self):
     self.driver.quit()
     self.assertEqual([], self.verificationErrors)
    if __name__ == "__main__":
        unittest.main()