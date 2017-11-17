# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os
#import win32gui
#import win32con

class Template_Enterise(unittest.TestCase):
    def setUp(self):
        # 设置浏览器的默认下载路径
        # profile.set_preference('browser.download.dir', 'D:\Python\pycharm_code\Local_Automation_Code\Download_file')
        # profile.set_preference('browser.download.folderList', 2)
        # profile.set_preference('browser.download.manager.showWhenStarting', False)
        # profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
        #                        'application/zip,text/plain,application/vnd.ms-excel,text/csv,text/comma-separated-values,application/octet-stream,'
        #                        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        profile = webdriver.FirefoxProfile()
        self.driver = webdriver.Firefox(firefox_profile=profile)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_2(self):
        driver = self.driver
        driver.get(self.base_url + "/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("1")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum0").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("div.fl-l.lead-btn").click()
        driver.implicitly_wait(30)
        driver.find_element_by_class_name("swfupload").click()
        driver.implicitly_wait(30)
        os.system("upload.exe")
        # #对话框
        # dialog = win32gui.FindWindow('#32770',u'打开')
        # #寻找对象，直到找到输入框edit对象的句柄
        # ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None)
        # ComboBox = win32gui.FindWindowEx(ComboBoxEx32,0,'ComboBox',None)
        # Edit = win32gui.FindWindowEx(ComboBox,0,'Edit',None)
        # #确定button
        # button = win32gui.FindWindowEx(dialog,0,'Button',None)
        # #输入地址
        # win32gui.SendMessage(Edit,win32con.WM_SETTEXT,None,'D:\\Python\\pycharm_code\\Local_Automation_Code\\Download_file\\template_Enterise.xls')
        # win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)
        #点击提交按钮
        driver.find_element_by_css_selector("input.upload-btn").click()
        #点击返回按钮
        time.sleep(40)
        driver.find_element_by_xpath("/html/body/ul/button[1]").click()
        #driver.find_element_by_css_selector("button.lead-btn").click()
       # driver.find_element_by_xpath("//div[@onclick=\"window.location.href='selectRemainList';\"]").click()
       # driver.find_element_by_css_selector("div.fl-l.lead-btn").click()
        #点击首页
        driver.implicitly_wait(20)
        driver.find_element_by_link_text(u"首页").click()
        driver.find_element_by_link_text(u"尾页").click()
        driver.find_element_by_link_text(u"首页").click()
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
