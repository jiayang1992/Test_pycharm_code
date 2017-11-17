# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class Template_Enterise(unittest.TestCase):
    def setUp(self):
        # profile = webdriver.FirefoxProfile()
        # #设置浏览器的默认下载路径
        # profile.set_preference('browser.download.dir','D:\Python\pycharm_code\Local_Automation_Code\Download_file')
        # profile.set_preference('browser.download.folderList',2)
        # profile.set_preference('browser.download.manager.showWhenStarting',False)
        # profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/zip,text/plain,application/vnd.ms-excel,text/csv,text/comma-separated-values,application/octet-stream,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        # self.driver = webdriver.Firefox(firefox_profile=profile)
        # self.driver.implicitly_wait(30)
        # self.base_url = "http://101.201.41.228:6800/manage/user/home"
        # self.verificationErrors = []
        # self.accept_next_alert = True

        # 设置浏览器的默认下载路径
        # options.set_preference('browser.download.dir', 'D:\Python\pycharm_code\Local_Automation_Code\Download_file')
        # options.set_preference('browser.download.folderList', 2)
        # options.set_preference('browser.download.manager.showWhenStarting', False)
        # options.set_preference('browser.helperApps.neverAsk.saveToDisk',
        #                        'application/zip,text/plain,application/vnd.ms-excel,text/csv,text/comma-separated-values,application/octet-stream,'
        #                        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        options = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': 'D:\\Python\\pycharm_code\\Local_Automation_Code\\Download_file\\',
                 'profile.default_content_setting_values.notifications':2,'profile.default_content_setting.flash':'allow'}
        options.add_experimental_option('prefs', prefs)
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver

        # driver.get("chrome://settings/content/siteDetails?site=http%3A%2F%2F101.201.41.228%3A6800")
        # driver.find_element_by_class_name("md-select-wrapper").click()
        # Select(driver.find_element_by_class_name("md-select")).select_by_value("allow")
        # driver.quit()
        driver.get(self.base_url + "/manage/user/home")
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.maximize_window()
        driver.find_element_by_css_selector("li.unnum0").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("div.fl-l.lead-btn").click()
        driver.find_element_by_xpath("//button[@onclick=\"window.location.href='../../excel/template_Enterise.xls';\"]").click()
        time.sleep(2)
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
