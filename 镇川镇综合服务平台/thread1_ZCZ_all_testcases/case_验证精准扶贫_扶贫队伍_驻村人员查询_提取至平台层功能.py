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
        driver.find_element_by_id("menu-sm2").click()
        driver.find_element_by_id("second-21").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"李")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_xpath("(//input[@name='ids'])[2]").click()
        driver.find_element_by_css_selector("input.save-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectDepartId"))
        driver.find_element_by_id("treeDemo_3_check").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        self.assertEqual(u"已成功提取至平台层!", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.switch_to_default_content()
        driver.find_element_by_css_selector("li.unnum10").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.find_element_by_id("second-01").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath(u"(//a[contains(text(),'成员管理')])[3]").click()
        driver.find_element_by_id("userNameId").click()
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"李浩清")
        driver.find_element_by_xpath("//form[@id='areaFormId']/div/ul/li[2]").click()
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以关键字'李浩清'查询到%d条结果" % int(value))
        # driver.find_element_by_link_text(u"查看").click()
        # time.sleep(5)
        # driver.find_element_by_id("closeId").click()
        # driver.find_element_by_link_text(u"编辑").click()
        # driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updCadreInfo"))
        # driver.find_element_by_id("closeId").click()
        # driver.switch_to_default_content()
        # driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此条干部信息吗[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此条干部信息吗[\s\S]$")
        self.assertEqual(u"信息删除成功!", self.close_alert_and_get_its_text())
        driver.find_element_by_id("userNameId").click()
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"李浩清")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("删除该成员信息后，以关键字'李浩清'查询到%d条结果" % int(value))
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
