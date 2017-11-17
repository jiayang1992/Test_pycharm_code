# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class System_User_Management(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(3)
        driver.find_element_by_css_selector("li.unnum2").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.find_element_by_id("second-01").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("jiayang")
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys("jiayang")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("telePhone").clear()
        #输入错的联系人
        driver.find_element_by_id("telePhone").send_keys("15709277263")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        #输入对的联系人
        driver.find_element_by_id("telePhone").clear()
        driver.find_element_by_id("telePhone").send_keys("15709277266")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_id("dstatus")).select_by_visible_text(u"有效")
        driver.find_element_by_id("queryBtn").click()
        Select(driver.find_element_by_id("dstatus")).select_by_visible_text(u"无效")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("jiayang")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^删除后将无法恢复,确定要删除吗[\s\S]$")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("jiayang")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("userCode").clear()
        driver.find_element_by_id("userCode").send_keys("101")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_id("newPassword2").clear()
        driver.find_element_by_id("newPassword2").send_keys("1")
        driver.find_element_by_name("radioRole").click()
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_css_selector("button.back-btn").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("userCode").clear()
        driver.find_element_by_id("userCode").send_keys("102")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_id("newPassword2").clear()
        driver.find_element_by_id("newPassword2").send_keys("1")
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_id("nativePlace").clear()
        driver.find_element_by_id("nativePlace").send_keys(u"陕西咸阳")
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        #driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1")
        driver.find_element_by_id("newPassword2").clear()
        driver.find_element_by_id("newPassword2").send_keys("1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("123456jy")
        driver.find_element_by_id("newPassword2").clear()
        driver.find_element_by_id("newPassword2").send_keys("123456jy")
        driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr[4]/td[2]/input[2]").click()
        driver.find_element_by_xpath("/html/body/form/table[2]/tbody/tr[5]/td[2]/input[3]").click()
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys("jiayang")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^删除后将无法恢复,确定要删除吗[\s\S]$")
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
