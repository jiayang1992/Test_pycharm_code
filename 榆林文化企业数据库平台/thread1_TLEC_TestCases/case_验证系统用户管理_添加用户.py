# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class User_Management_2(unittest.TestCase):
    def setUp(self):
        options =webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': 'D:\\Python\\pycharm_code\\Local_Automation_Code\\Download_file\\'}
        options.add_experimental_option('prefs', prefs)
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_2(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(self.base_url)
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum2").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.find_element_by_id("second-01").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        time.sleep(3)
        driver.find_element_by_css_selector("input.form-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='atrDialogIframe_addCadreInfo']"))
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys("jiayang")
        Select(driver.find_element_by_id("sex")).select_by_visible_text(u"女")
        driver.find_element_by_id("idCard").clear()
        driver.find_element_by_id("idCard").send_keys("610126199201031425")
        driver.find_element_by_id("telPhone").clear()
        driver.find_element_by_id("telPhone").send_keys("15709277266")
        driver.find_element_by_id("faimlyAddress").clear()
        driver.find_element_by_id("faimlyAddress").send_keys(u"中国")
        driver.find_element_by_id("remark").send_keys(u"陕西西安")
        driver.find_element_by_id("SWFUpload_0").click()
        os.system("uploadpicture.exe")
        # self.accept_next_alert = False
        time.sleep(10)
        driver.find_element_by_link_text(u"[删除]").click()
        self.accept_next_alert = False
        self.assertEqual(u"你确定永久删除此图片吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"[删除]").click()
        self.assertEqual(u"你确定永久删除此图片吗？", self.close_alert_and_get_its_text())
        self.accept_next_alert = True
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"信息保存成功!", self.close_alert_and_get_its_text())
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("input.form-btn").click()
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='atrDialogIframe_addCadreInfo']"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"退出").click()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("111111")
    
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
