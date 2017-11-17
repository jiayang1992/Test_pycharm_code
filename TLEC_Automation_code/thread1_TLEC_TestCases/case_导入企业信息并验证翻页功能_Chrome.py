# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import unittest, time, re, os


class Template_Enterise(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        # 设置浏览器的默认下载路径及弹出窗口
        prefs = {'profile.default_content_settings.popups':0,'download.default_directory':'D:\\Python\\pycharm_code\\Local_Automation_Code\\Download_file\\'}
        option.add_experimental_option('prefs',prefs)
        #指定chromediver的位置，如果在默认路径，这两行可以省略。
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = executable_path
        option.add_argument("--user-data-dir="+r"D:\Python\pycharm_code\Local_Automation_Code\TLEC_Automation_code\Google\Chrome\User Data")
        #指定用户的配置地址，并加载至配置对象中。
        self.driver = webdriver.Chrome(executable_path,chrome_options=option)
       # self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_2(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(10)
        driver.find_element_by_css_selector("li.unnum0").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        #点击导入企业信息
        driver.find_element_by_css_selector("div.fl-l.lead-btn").click()
        time.sleep(2)
        driver.find_element_by_class_name("swfupload").click()
        #driver.find_elements_by_id("uploadify-button").click()
        time.sleep(10)
        os.system("upload.exe")
        driver.find_element_by_css_selector("input.upload-btn").click()
        time.sleep(10)
        driver.find_element_by_css_selector("button.lead-btn").click()
        #driver.find_element_by_xpath("//div[@onclick=\"window.location.href='selectRemainList';\"]").click()
        #driver.find_element_by_css_selector("div.fl-l.lead-btn").click()
        driver.implicitly_wait(20)
        driver.find_element_by_link_text(u"下一页").click()
        driver.find_element_by_link_text(u"上一页").click()
        driver.find_element_by_link_text(u"首页").click()
        driver.find_element_by_link_text(u"尾页").click()
        driver.find_element_by_id("topageNo").send_keys("1")
        driver.find_element_by_class_name("page-btn").click()
        #查看导入失败数据
        driver.find_element_by_xpath("/html/body/form/div[3]").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"下一页").click()
        driver.find_element_by_link_text(u"上一页").click()
        driver.find_element_by_link_text(u"首页").click()
        driver.find_element_by_link_text(u"尾页").click()
        driver.find_element_by_id("topageNo").send_keys("1")
        driver.find_element_by_class_name("page-btn").click()
        driver.find_element_by_css_selector("div.fl-l.lead-btn").click()
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"退出").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
