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
        driver.find_element_by_id("second-73").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_css_selector("input.edit-btn").click()
        driver.find_element_by_id("logName").clear()
        driver.find_element_by_id("logName").send_keys(u"测试")
        driver.find_element_by_id("logContent").click()
        driver.find_element_by_id("logContent").clear()
        driver.find_element_by_id("logContent").send_keys(u"测试")
        driver.find_element_by_id("file-1").click()
        # driver.find_element_by_class_name("glyphicon glyphicon-folder-open").click()
        os.system("uploadpicture.exe")
        driver.find_element_by_css_selector("button.kv-file-upload.btn.btn-xs.btn-default").click()
        driver.find_element_by_id("1517392776354644").click()
        driver.find_element_by_id("1517392776354644").clear()
        driver.find_element_by_id("1517392776354644").send_keys("11")
        driver.find_element_by_link_text(u"上传").click()
        driver.find_element_by_css_selector("button.kv-file-remove.btn.btn-xs.btn-default").click()
        driver.find_element_by_id("file-1").click()
        os.system("uploadpicture.exe")
        driver.find_element_by_css_selector("button.kv-file-upload.btn.btn-xs.btn-default").click()
        driver.find_element_by_css_selector("div.clearfix").click()
        driver.find_element_by_id("1517392792843391").click()
        driver.find_element_by_id("1517392792843391").clear()
        driver.find_element_by_id("1517392792843391").send_keys("11")
        driver.find_element_by_link_text(u"上传").click()
        driver.find_element_by_css_selector("button.btn.btn-default.fileinput-remove.fileinput-remove-button").click()
        driver.find_element_by_id("file-1").click()
        os.system("uploadpicture.exe")
        driver.find_element_by_css_selector("i.glyphicon.glyphicon-hand-down.text-warning").click()
        driver.find_element_by_css_selector("button.kv-file-upload.btn.btn-xs.btn-default").click()
        driver.find_element_by_id("1517392813357802").click()
        driver.find_element_by_id("1517392813357802").clear()
        driver.find_element_by_id("1517392813357802").send_keys("11")
        driver.find_element_by_css_selector("button.kv-file-upload.btn.btn-xs.btn-default").click()
        driver.find_element_by_id("1517392817507710").click()
        driver.find_element_by_id("1517392817507710").clear()
        driver.find_element_by_id("1517392817507710").send_keys("11")
        driver.find_element_by_link_text(u"上传").click()
        driver.find_element_by_id("1517392821454537").click()
        driver.find_element_by_id("1517392821454537").clear()
        driver.find_element_by_id("1517392821454537").send_keys("11")
        driver.find_element_by_css_selector("a.btn.btn-default.kv-fileinput-upload.fileinput-upload-button > i.glyphicon.glyphicon-upload").click()
        driver.find_element_by_id("leaderTag").click()
        driver.find_element_by_id("leaderTag").clear()
        driver.find_element_by_id("leaderTag").send_keys(u"张泽，王博")
        driver.find_element_by_css_selector("input.save-btn").click()
        driver.find_element_by_id("1517392829519467").click()
        driver.find_element_by_id("1517392829519467").clear()
        driver.find_element_by_id("1517392829519467").send_keys("11")
        driver.find_element_by_css_selector("input.save-btn").click()
        driver.find_element_by_css_selector("input.save-btn").click()
        driver.find_element_by_css_selector("input.save-btn").click()
        driver.find_element_by_id("logContent").click()
        driver.find_element_by_id("logContent").clear()
        driver.find_element_by_id("logContent").send_keys(u"测试镇川综合服务平台绩效考核")
        driver.find_element_by_css_selector("input.save-btn").click()
        driver.find_element_by_name("departName").click()
        driver.find_element_by_name("departName").click()
        driver.find_element_by_name("logUserName").click()
        driver.find_element_by_name("logUserName").clear()
        driver.find_element_by_name("logUserName").send_keys(u"李")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("familyUserName").click()
        driver.find_element_by_name("familyUserName").clear()
        driver.find_element_by_name("familyUserName").send_keys(u"王")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("startDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("endDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("searchIndex").click()
        driver.find_element_by_id("searchIndex").click()
        driver.find_element_by_name("searchKey").click()
        driver.find_element_by_name("searchKey").clear()
        driver.find_element_by_name("searchKey").send_keys(u"测试")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
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
