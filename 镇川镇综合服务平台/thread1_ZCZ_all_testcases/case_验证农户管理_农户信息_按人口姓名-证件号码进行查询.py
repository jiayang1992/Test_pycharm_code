# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class Case(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path, chrome_options=option)
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.115.106.140:7001/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum1").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"高")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以人口姓名'高'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"沈")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以人口姓名'沈'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"候秀武")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以不存在的人口姓名'候秀武'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"候")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"侯武秀")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以人口姓名'侯武秀'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"常文厚")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以人口姓名'常文厚'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"樊世纪")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以人口姓名'樊世纪'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("610")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以证件号码'610'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("612")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以证件号码'612'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("613")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以不存在的证件号码'613'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("6102119531")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以证件号码'6102119531'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("6127211")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以证件号码'6127211'关键字搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
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
