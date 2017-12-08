# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class Cese(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=option)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:7006/ylsn1.5/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_cese(self):
        driver = self.driver
        driver.get(self.base_url + "/ylsn1.5/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum0").click()
        driver.find_element_by_id("menu-sm2").click()
        driver.find_element_by_id("second-20").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_link_text(u"名人榜管理").click()
        driver.find_element_by_css_selector("button.edit-btn").click()
        Select(driver.find_element_by_id("starTypeCode")).select_by_visible_text(u"军人")
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"张荣姬")
        driver.find_element_by_id("introduce").clear()
        driver.find_element_by_id("introduce").send_keys(u"测试")
        driver.find_element_by_class_name("swfupload").click()
        os.system("uploadpicture.exe")
        time.sleep(3)
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual("0", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_css_selector("button.edit-btn").click()
        driver.find_element_by_id("backBtn").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("introduce").clear()
        driver.find_element_by_id("introduce").send_keys(u"测试01")
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"张荣姬")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("resetBtn").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"确定要删除吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"确定要删除吗？", self.close_alert_and_get_its_text())
        time.sleep(3)
        self.assertEqual(u"删除成功", self.close_alert_and_get_its_text())
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
