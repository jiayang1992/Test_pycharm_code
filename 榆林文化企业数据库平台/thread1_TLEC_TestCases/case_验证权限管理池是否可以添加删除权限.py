# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class Management_Pool(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum2").click()
        driver.find_element_by_id("menu-sm2").click()
        driver.find_element_by_id("second-20").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("button.edit-btn").click()
        driver.find_element_by_id("acceptUrl").clear()
        driver.find_element_by_id("acceptUrl").send_keys("http://101.201.41.228:6800/manage/user/home?isShowAlert=0")
        driver.find_element_by_name("mouldDesc").clear()
        driver.find_element_by_name("mouldDesc").send_keys(u"榆林文化")
        driver.find_element_by_css_selector("button.save-btn").click()
        Select(driver.find_element_by_name("isUse")).select_by_visible_text(u"有效")
        driver.find_element_by_id("queryData").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[3]").click()
        driver.find_element_by_id("saveRoleBtn").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"退出").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
