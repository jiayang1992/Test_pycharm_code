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
        driver.find_element_by_id("second-70").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("toAddBtn").click()
        currnet_driver = driver.current_window_handle
        driver.find_element_by_id("personName").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='Mesframe']"))
        time.sleep(3)
        windows_driver = driver.window_handles
        for logwin_driver in windows_driver:
            if logwin_driver != currnet_driver:
                driver.switch_to_window(logwin_driver)
        # element0 = driver.find_elements_by_id("treeDemo_1_switch")
        # for elem0 in element0:
        #     if elem0.is_displayed():
        #         elem0.click()
        driver.find_element_by_id("treeDemo_1_switch").click()
        driver.find_element_by_id("treeDemo_5_switch").click()
        driver.find_element_by_id("treeDemo_6_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("id0").click()
        driver.find_element_by_id("Submit").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_id("month").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_name("pacesetterState").click()
        driver.find_element_by_name("pacesetterState").click()
        driver.find_element_by_name("summary").click()
        driver.find_element_by_name("summary").clear()
        driver.find_element_by_name("summary").send_keys(u"测试")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_link_text(u"王雨皓").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_id("switch-big5").click()
        driver.find_element_by_id("switch-big6").click()
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_css_selector("input.dialog-btn").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_name("dosubmit").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        driver.find_element_by_id("villageId").click()
        driver.find_element_by_id("villageId").click()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"张东东")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("month").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_css_selector("td.menuOn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("month").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_css_selector("td.menuOn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_xpath("//form[@id='pacesetterFormId']/div/ul/li[3]").click()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"张东东")
        driver.find_element_by_id("queryBtn").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
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
