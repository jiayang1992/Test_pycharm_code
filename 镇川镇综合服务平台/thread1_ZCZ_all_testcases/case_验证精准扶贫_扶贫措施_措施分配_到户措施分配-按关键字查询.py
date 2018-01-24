# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path, chrome_options=option)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://124.115.106.140:7001/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").click()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").click()
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("1")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum4").click()
        driver.find_element_by_id("menu-sm3").click()
        driver.find_element_by_id("second-31").click()
        driver.find_element_by_css_selector("#level-31 > ul > #menuli11").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"樊世纪")
        driver.find_element_by_xpath("//form[@id='familysForm']/ul/li[15]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("cardNo").click()
        driver.find_element_by_name("cardNo").clear()
        driver.find_element_by_name("cardNo").send_keys("61272119410205")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("hasnotHelpPerson").click()
        Select(driver.find_element_by_name("hasnotHelpPerson")).select_by_visible_text(u"未设置")
        driver.find_element_by_css_selector("select[name=\"hasnotHelpPerson\"] > option[value=\"0\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("hasnotHelpPerson").click()
        Select(driver.find_element_by_name("hasnotHelpPerson")).select_by_visible_text(u"已设置")
        driver.find_element_by_css_selector("select[name=\"hasnotHelpPerson\"] > option[value=\"1\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("helpPersonName").click()
        driver.find_element_by_id("helpPersonName").clear()
        driver.find_element_by_id("helpPersonName").send_keys(u"马志平")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("helpPersonName").click()
        driver.find_element_by_id("helpPersonName").clear()
        driver.find_element_by_id("helpPersonName").send_keys(u"白雪榕")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("methodId").click()
        # Select(driver.find_element_by_id("methodId")).select_by_visible_text(u"regexp:\\s+村级修路政策")
        Select(driver.find_element_by_id("methodId")).select_by_value("1516689593264893")
        driver.find_element_by_css_selector("option[value=\"1516689593264893\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("methodId").click()
        Select(driver.find_element_by_id("methodId")).select_by_visible_text("")
        driver.find_element_by_css_selector("option[value=\"50001\"]").click()
        self.assertEqual(u"请选择 兜底保障 下的子类进行查询!", self.close_alert_and_get_its_text())
        driver.find_element_by_id("methodId").click()
        # Select(driver.find_element_by_id("methodId")).select_by_visible_text(u"regexp:\\s+临时性医疗救助")
        Select(driver.find_element_by_id("methodId")).select_by_value("5000101")
        driver.find_element_by_css_selector("option[value=\"5000101\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("queryMyObject").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
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
