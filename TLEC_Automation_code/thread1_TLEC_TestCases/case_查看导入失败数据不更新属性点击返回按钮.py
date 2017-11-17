# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import os


class Re_import_data(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        prefs = {'profile.default_content_settings.popups': 0,
                 'download.default_directory': 'D:\\Python\\pycharm_code\\Local_Automation_Code\\Download_file\\'}
        option.add_experimental_option('prefs', prefs)
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = executable_path
        self.driver = webdriver.Chrome(executable_path, chrome_options=option)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum0").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # 查看导入失败数据
        driver.find_element_by_xpath("/html/body/form/div[3]").click()
        # driver.find_element_by_xpath("//div[@onclick=\"window.location.href='selectRemainList';\"]").click()
        driver.find_element_by_id("firstCheckbox").click()
        driver.find_element_by_name("ids").click()
        driver.find_element_by_link_text(u"查看").click()
        Select(driver.find_element_by_name("depId")).select_by_value("1502184891122993")
        Select(driver.find_element_by_name("industryBaseCodeId")).select_by_value("2222")
        Select(driver.find_element_by_name("enterTypeBaseCodeId")).select_by_value("1501057775003642")
        Select(driver.find_element_by_name("industryTypeBaseCodeId")).select_by_value("2311")
        Select(driver.find_element_by_name("enterpriseTypeBaseCodeId")).select_by_value("1501140245842149")
        driver.find_element_by_css_selector("button.back-btn").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div.fl-l.lead-btn").click()
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"退出").click()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("111111")

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
