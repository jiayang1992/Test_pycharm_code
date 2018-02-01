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
        driver.find_element_by_id("second-42").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_css_selector("img.cursor").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='Mesframe']"))
        driver.find_element_by_xpath("//*[@id='name']").click()
        driver.find_element_by_xpath("//*[@id='name']").clear()
        driver.find_element_by_xpath("//*[@id='name']").send_keys(u"唐")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("id0").click()
        driver.find_element_by_id("Submit").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.find_element_by_id("610802028001").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_villageId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
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
        driver.find_element_by_id("switch-big16").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("closeId").click()
        driver.find_element_by_id("fid0").click()
        driver.find_element_by_xpath("//img[@onclick=\"WdatePicker({el:'startTimes0',dateFmt:'yyyy-MM-dd'})\"]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[5]/td[5]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("button.set-btn").click()
        driver.find_element_by_name("town").click()
        driver.find_element_by_name("town").click()
        driver.find_element_by_name("villageName").click()
        driver.find_element_by_name("villageName").clear()
        driver.find_element_by_name("villageName").send_keys(u"八")
        driver.find_element_by_name("villager").click()
        driver.find_element_by_name("villager").clear()
        driver.find_element_by_name("villager").send_keys(u"唐")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("villageName").click()
        driver.find_element_by_name("villageName").clear()
        driver.find_element_by_name("villageName").send_keys(u"八")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("villager").click()
        driver.find_element_by_name("villager").clear()
        driver.find_element_by_name("villager").send_keys(u"张")
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
