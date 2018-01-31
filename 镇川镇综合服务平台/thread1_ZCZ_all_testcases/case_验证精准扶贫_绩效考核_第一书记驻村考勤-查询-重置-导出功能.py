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
        driver.find_element_by_id("menu-sm7").click()
        driver.find_element_by_id("second-71").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_name("town").click()
        driver.find_element_by_name("town").click()
        driver.find_element_by_id("villageId").click()
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        driver.find_element_by_css_selector("option[value=\"610802028001\"]").click()
        driver.find_element_by_css_selector("button.btn.btn-sm.btn-primary").click()
        driver.find_element_by_link_text(u"重置").click()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"张")
        driver.find_element_by_css_selector("button.btn.btn-sm.btn-primary").click()
        driver.find_element_by_link_text(u"重置").click()
        driver.find_element_by_id("startCheckNum").clear()
        driver.find_element_by_id("startCheckNum").send_keys("1")
        driver.find_element_by_id("endCheckNum").click()
        driver.find_element_by_id("endCheckNum").clear()
        driver.find_element_by_id("endCheckNum").send_keys("20")
        driver.find_element_by_css_selector("button.btn.btn-sm.btn-primary").click()
        driver.find_element_by_link_text(u"重置").click()
        driver.find_element_by_id("startCheckNum").clear()
        driver.find_element_by_id("startCheckNum").send_keys("g")
        driver.find_element_by_id("endCheckNum").click()
        driver.find_element_by_id("endCheckNum").clear()
        driver.find_element_by_id("endCheckNum").send_keys("f")
        driver.find_element_by_xpath("//form[@id='dysjCheckFormId']/table/tbody/tr[2]/td").click()
        driver.find_element_by_css_selector("button.btn.btn-sm.btn-primary").click()
        driver.find_element_by_css_selector("i.icon-exclamation-sign.icon-white").click()
        driver.find_element_by_id("startDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("endDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_css_selector("button.btn.btn-sm.btn-primary").click()
        driver.find_element_by_link_text(u"导出").click()
        time.sleep(5)
        driver.find_element_by_link_text(u"重置").click()
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
