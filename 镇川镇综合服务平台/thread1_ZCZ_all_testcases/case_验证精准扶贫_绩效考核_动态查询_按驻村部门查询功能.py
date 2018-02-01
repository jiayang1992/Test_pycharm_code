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
        driver.find_element_by_id("second-74").click()
        driver.find_element_by_id("menuli14").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_link_text(u"点此返回").click()
        driver.find_element_by_name("departPid").click()
        Select(driver.find_element_by_name("departPid")).select_by_visible_text(u"省级部门")
        driver.find_element_by_css_selector("option[value=\"1001\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("departPid").click()
        Select(driver.find_element_by_name("departPid")).select_by_visible_text(u"市级部门")
        driver.find_element_by_css_selector("option[value=\"1002\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("departPid").click()
        Select(driver.find_element_by_name("departPid")).select_by_visible_text(u"县级部门")
        driver.find_element_by_css_selector("option[value=\"1003\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath("(//a[contains(text(),'1')])[2]").click()
        driver.find_element_by_link_text(u"点此返回").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("depName").click()
        driver.find_element_by_name("depName").clear()
        driver.find_element_by_name("depName").send_keys(u"榆阳")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("depName").click()
        driver.find_element_by_name("depName").clear()
        driver.find_element_by_name("depName").send_keys(u"区人社")
        driver.find_element_by_name("depName").send_keys(Keys.DOWN)
        driver.find_element_by_name("depName").send_keys(Keys.DOWN)
        driver.find_element_by_name("depName").send_keys(Keys.ENTER)
        driver.find_element_by_name("depName").send_keys(Keys.ENTER)
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='导出']").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("startDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/div[6]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/div[6]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[7]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("endDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[4]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
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
