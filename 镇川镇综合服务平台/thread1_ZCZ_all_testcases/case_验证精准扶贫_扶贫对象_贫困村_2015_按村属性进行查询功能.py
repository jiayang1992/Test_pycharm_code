# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class Case2015(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path, chrome_options=option)
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.115.106.140:7001/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case2015(self):
        driver = self.driver
        driver.get(self.base_url + "/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum4").click()
        driver.find_element_by_id("menu-sm1").click()
        driver.find_element_by_id("second-11").click()
        driver.find_element_by_id("menuli01").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_id("villageAttriId")).select_by_visible_text(u"贫困村")
        Select(driver.find_element_by_name("alterYear")).select_by_visible_text(u"2015年度")
        driver.find_element_by_name("villageName").clear()
        driver.find_element_by_name("villageName").send_keys(u"八")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2015年度贫困村以关键字'八'进行查询，查询到%d个结果"%int(value))
        driver.find_element_by_xpath("//button[@type='button']").click()
        Select(driver.find_element_by_id("villageAttriId")).select_by_visible_text(u"贫困村")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2015年度贫困村进行查询，查询到%d个结果" % int(value))
        driver.find_element_by_xpath("//button[@type='button']").click()
        Select(driver.find_element_by_id("villageAttriId")).select_by_visible_text(u"非贫困村")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2015年度非贫困村进行查询，查询到%d个结果" % int(value))
        driver.find_element_by_xpath("//button[@type='button']").click()
        Select(driver.find_element_by_id("villageAttriId")).select_by_visible_text(u"经济薄弱村")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2015年度经济薄弱村进行查询，查询到%d个结果" % int(value))
        driver.find_element_by_xpath("//button[@type='button']").click()
        Select(driver.find_element_by_id("villageAttriId")).select_by_visible_text(u"十二五贫困村")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2015年度十二五贫困村进行查询，查询到%d个结果" % int(value))
        driver.find_element_by_xpath("//button[@type='button']").click()
        Select(driver.find_element_by_id("villageAttriId")).select_by_visible_text(u"十三五贫困村")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2015年度十三五贫困村进行查询，查询到%d个结果" % int(value))
        driver.find_element_by_xpath("//button[@type='button']").click()
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
