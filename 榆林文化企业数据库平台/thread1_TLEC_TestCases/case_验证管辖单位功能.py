# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class Jurisdictional_units(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum0").click()
        time.sleep(5)
        driver.find_element_by_id("menu-sm1").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("depName").clear()
        driver.find_element_by_id("depName").send_keys(u"绥德县工商行政管理局")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"绥德县工商行政管理局").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_id("depName").clear()
        time.sleep(2)
        driver.find_element_by_id("depName").send_keys(u"陕鼓动力")
        driver.find_element_by_id("address").clear()
        driver.find_element_by_id("address").send_keys(u"陕西西安")
        time.sleep(5)
        driver.find_element_by_id("saveRoleBtn").click()
        time.sleep(2)
        self.assertEqual(u"新增成功!", self.close_alert_and_get_its_text())
        time.sleep(3)
        driver.find_element_by_id("depName").clear()
        driver.find_element_by_id("depName").send_keys(u"陕鼓动力")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"陕鼓动力").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("depName").clear()
        driver.find_element_by_id("depName").send_keys(u"陕鼓动力")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(2)
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除当前部门吗[\s\S]$")
        time.sleep(2)
        driver.find_element_by_id("resetBtn").click()
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"退出").click()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("111111")
    
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
