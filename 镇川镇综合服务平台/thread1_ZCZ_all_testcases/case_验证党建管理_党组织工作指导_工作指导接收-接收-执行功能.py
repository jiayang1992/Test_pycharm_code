# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os


class Case(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path, chrome_options=option)
        self.driver.implicitly_wait(30)
        self.base_url = "http://124.115.106.140:7001/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum3").click()
        driver.find_element_by_id("menu-sm3").click()
        driver.find_element_by_id("second-31").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_1_span").click()
        driver.find_element_by_id("partGroupTree_1_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("partGroupTree_4_span").click()
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        value2 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("工作指导接收下共有%d条消息" % int(value2))
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"接收").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定接收此党组织工作指导信息吗[\s\S]$")
        driver.find_element_by_link_text(u"接收").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定接收此党组织工作指导信息吗[\s\S]$")
        self.assertEqual(u"接收成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"执行").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewpartyWorkRecId"))
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"确定成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # driver.switch_to_default_content()
        # driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        # driver.find_element_by_link_text(u"执行").click()
        # driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewpartyWorkRecId"))
        # # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # driver.find_element_by_css_selector("li > #closeId").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        # driver.switch_to_default_content()
        # driver.find_element_by_id("second-30").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        # driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # driver.find_element_by_id("partGroupTree_1_span").click()
        # driver.find_element_by_id("partGroupTree_1_switch").click()
        # driver.find_element_by_id("partGroupTree_4_span").click()
        # driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        # self.accept_next_alert = False
        # driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[1]").click()
        # self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此党组织工作指导信息吗[\s\S]$")
        # driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[1]").click()
        # self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此党组织工作指导信息吗[\s\S]$")
        # self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        # driver.switch_to_default_content()
        #driver.find_element_by_link_text(u"退出").click()

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
