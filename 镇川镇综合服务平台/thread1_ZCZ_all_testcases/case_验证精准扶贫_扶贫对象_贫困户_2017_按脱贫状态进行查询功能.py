# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os


class Case2017(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path, chrome_options=option)
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.115.106.140:7001/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case2017(self):
        driver = self.driver
        driver.get(self.base_url + "/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum4").click()
        driver.find_element_by_id("menu-sm1").click()
        driver.find_element_by_id("second-10").click()
        driver.find_element_by_id("menuli20").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_id("alterYearId")).select_by_visible_text(u"2017年度")
        Select(driver.find_element_by_id("tpAttriId")).select_by_visible_text(u"未脱贫")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2017年未脱贫有%d人" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        Select(driver.find_element_by_id("tpAttriId")).select_by_visible_text(u"已脱贫（享受政策）")
        Select(driver.find_element_by_id("alterYearId")).select_by_visible_text(u"2017年度")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2017年已脱贫（享受政策）有%d人" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        Select(driver.find_element_by_id("alterYearId")).select_by_visible_text(u"2017年度")
        Select(driver.find_element_by_id("tpAttriId")).select_by_visible_text(u"预脱贫")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2017年预脱贫有%d人" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        Select(driver.find_element_by_id("alterYearId")).select_by_visible_text(u"2017年度")
        Select(driver.find_element_by_id("tpAttriId")).select_by_visible_text(u"返贫")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2017年返贫有%d人" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        Select(driver.find_element_by_id("alterYearId")).select_by_visible_text(u"2017年度")
        Select(driver.find_element_by_id("tpAttriId")).select_by_visible_text(u"已脱贫（不再享受政策）")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("2017年已脱贫（不再享受政策)有%d人" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
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
