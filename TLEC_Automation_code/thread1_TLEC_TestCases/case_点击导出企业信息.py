# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class ClickExportEnterise(unittest.TestCase):
    def setUp(self):
        # profile = webdriver.FirefoxProfile()
        # # 设置浏览器的默认下载文件夹以及路径
        # profile.set_preference('browser.download.lastDir','D:\Python\pycharm_code\Local_Automation_Code\Download_file')
        # profile.set_preference('browser.download.dir', 'D:\Python\pycharm_code\Local_Automation_Code\Download_file')
        # profile.set_preference('browser.download.useDownloadDir', True)
        # # browser.download.folderList 设置Firefox的默认 下载 文件夹。0是桌面；1是“我的下载”；2是自定义
        # profile.set_preference('browser.download.folderList', 2)
        # # 设置是否显示下载进度框
        # profile.set_preference('browser.download.manager.showWhenStarting', False)
        # #profile.set_preference('browser.download.panel.shown', False)
        # # 设置哪种类型的文件下载不询问直接下载
        # profile.set_preference('browser.helperApps.neverAsk.saveToDisk',
        #                        'application/zip,text/plain,application/vnd.ms-excel,text/csv,text/comma-separated-values,application/octet-stream,application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        # # fp = webdriver.FirefoxProfile("D:\Python")
        # self.driver = webdriver.Firefox(firefox_profile=profile)
        # self.driver.implicitly_wait(30)
        # self.base_url = "http://101.201.41.228:6800/manage/user/home"
        # self.verificationErrors = []
        # self.accept_next_alert = True
        options = webdriver.ChromeOptions()
        # 设置浏览器的默认下载文件夹以及路径
        # browser.download.folderList 设置Firefox的默认 下载 文件夹。0是桌面；1是“我的下载”；2是自定义
        # 设置是否显示下载进度框
        # profile.set_preference('browser.download.panel.shown', False)
        # 设置哪种类型的文件下载不询问直接下载
        prefs = {'download.default_directory': 'D:\\Python\\pycharm_code\\Local_Automation_Code\\Download_file\\',
                 'browser.download.folderList':2,
                 'browser.download.useDownloadDir':True,
                 'browser.download.manager.showWhenStarting':False,
                 'plugin.state.flash': 2,
                 'plugins.flashBlock.enabled':'false'}
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
        driver.get(self.base_url + "/manage/user/home")
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.maximize_window()
        driver.find_element_by_css_selector("li.unnum0").click()
        time.sleep(2)
        driver.find_element_by_id("menu-sm0").click()
        time.sleep(10)
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath("/html/body/form/div[2]").click()
        time.sleep(5)
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
