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
        driver.find_element_by_id("menu-sm4").click()
        driver.find_element_by_id("second-41").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_link_text(u"设置帮扶责任人").click()
        driver.find_element_by_id("addHelpPerson").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectPerson"))
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"王")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("id1").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_class_name("aui_state_highlight").click()
        driver.find_element_by_id("hs_startTime5").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[5]/td[5]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("hs_endTime5").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[5]/td[6]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_link_text("保存设置").click()
        time.sleep(2)
        driver.find_element_by_css_selector("button[type=\"button\"]").click()
        driver.find_element_by_css_selector("button.set-btn").click()
        driver.find_element_by_link_text(u"设置帮扶责任人").click()
        driver.find_element_by_id("addHelpPerson").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button.set-btn").click()
        driver.find_element_by_link_text("查看").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_id("switch-big5").click()
        driver.find_element_by_id("switch-big6").click()
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_css_selector("input.dialog-btn").click()
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        time.sleep(3)
        driver.find_element_by_link_text(u"比对").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_compareId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        # driver.find_element_by_xpath("//div[@id='switch-sm1']/table/tbody/tr[2]/td[2]").click()
        driver.find_element_by_css_selector("button.dialog-btn").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        time.sleep(3)
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_link_text(u"设置帮扶责任人").click()
        driver.find_element_by_link_text(u"解除关系").click()
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"解除关系").click()
        driver.find_element_by_css_selector("button[type=\"button\"]").click()
        time.sleep(3)
        self.assertEqual(u"解除帮扶结对关系成功!", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("button.set-btn").click()
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
