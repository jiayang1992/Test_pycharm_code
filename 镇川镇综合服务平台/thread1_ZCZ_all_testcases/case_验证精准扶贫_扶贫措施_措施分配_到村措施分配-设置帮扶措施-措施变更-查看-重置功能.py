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
        driver.find_element_by_css_selector("#level-31 > ul > #menuli01").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("setHelpMethods").click()
        self.assertEqual(u"请先选择要操作的内容！", self.close_alert_and_get_its_text())
        driver.find_element_by_id("fid1").click()
        driver.find_element_by_id("setHelpMethods").click()
        driver.find_element_by_id("oneKeyAdd").click()
        driver.find_element_by_link_text(u"添加").click()
        self.assertEqual(u"重复添加!", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"一键重置").click()
        driver.find_element_by_link_text(u"一键设置").click()
        # driver.find_element_by_xpath("/html/body/div[8]/table/tbody/tr[2]/td[3]/div/ul/li/a").click()
        # driver.find_element_by_xpath("//*[@id='1497510670873739']").click()
        driver.find_element_by_link_text(u"保存设置").click()
        time.sleep(3)
        self.assertEqual(u"设置成功!", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath(u"(//a[contains(text(),'措施变更')])[2]").click()
        driver.find_element_by_link_text(u"添加").click()
        self.assertEqual(u"重复添加!", self.close_alert_and_get_its_text())
        # driver.find_element_by_css_selector("#operateMethod > #1497510670873739 > a").click()
        driver.find_element_by_xpath("/html/body/div[8]/table/tbody/tr[2]/td[3]/div/ul/li/a").click()
        driver.find_element_by_link_text(u"添加").click()
        driver.find_element_by_link_text(u"一键添加").click()
        driver.find_element_by_link_text(u"保存更改").click()
        time.sleep(3)
        self.assertEqual(u"设置成功!", self.close_alert_and_get_its_text())

        driver.find_element_by_xpath(u"(//a[contains(text(),'措施变更')])[2]").click()
        driver.find_element_by_link_text(u"一键添加").click()
        driver.find_element_by_link_text(u"移除").click()
        driver.find_element_by_link_text(u"一键添加").click()
        driver.find_element_by_link_text(u"保存更改").click()
        time.sleep(3)
        self.assertEqual(u"设置成功!", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"措施变更").click()
        driver.find_element_by_css_selector("div.sm-dialog-close").click()
        driver.find_element_by_id("610802028002").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_villageId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_id("switch-big5").click()
        driver.find_element_by_id("switch-big6").click()
        driver.find_element_by_id("switch-big7").click()
        driver.find_element_by_id("switch-big8").click()
        driver.find_element_by_id("switch-big9").click()
        driver.find_element_by_id("switch-big10").click()
        driver.find_element_by_id("switch-big11").click()
        driver.find_element_by_id("switch-big12").click()
        driver.find_element_by_id("switch-big13").click()
        driver.find_element_by_id("switch-big14").click()
        driver.find_element_by_id("switch-big17").click()
        driver.find_element_by_id("switch-big15").click()
        driver.find_element_by_id("switch-big18").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'查看')])[5]").click()
        driver.find_element_by_id("closeId").click()
        time.sleep(2)
        driver.find_element_by_id("switch-big16").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("closeId").click()
        time.sleep(3)
        driver.find_element_by_name("villageName").click()
        driver.find_element_by_name("villageName").clear()
        driver.find_element_by_name("villageName").send_keys(u"陈")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("villager").click()
        driver.find_element_by_name("villager").clear()
        driver.find_element_by_name("villager").send_keys(u"陈")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("methodId").click()
        Select(driver.find_element_by_id("methodId")).select_by_value("1497510670873739")
        driver.find_element_by_css_selector("option[value=\"1497510670873739\"]").click()
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
