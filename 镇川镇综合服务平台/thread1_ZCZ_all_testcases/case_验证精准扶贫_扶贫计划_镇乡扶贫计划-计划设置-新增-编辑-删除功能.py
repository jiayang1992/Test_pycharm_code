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
        driver.find_element_by_xpath("//form[@id='formLogin']/table/tbody/tr/td[3]").click()
        driver.find_element_by_id("userNameCopy").click()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").click()
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("1")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum4").click()
        driver.find_element_by_id("menu-sm4").click()
        driver.find_element_by_id("second-43").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_link_text(u"计划设置").click()
        driver.find_element_by_css_selector("button.back-btn").click()
        driver.find_element_by_link_text(u"计划设置").click()
        driver.find_element_by_id("addBtn").click()
        driver.find_element_by_id("tpYear").click()
        Select(driver.find_element_by_id("tpYear")).select_by_visible_text(u"2017年度")
        driver.find_element_by_css_selector("option[value=\"2017\"]").click()
        driver.find_element_by_id("totalPoorVillages").click()
        driver.find_element_by_id("totalPoorVillages").clear()
        driver.find_element_by_id("totalPoorVillages").send_keys("58")
        driver.find_element_by_id("totalPoorFamilys").click()
        driver.find_element_by_id("totalPoorFamilys").clear()
        driver.find_element_by_id("totalPoorFamilys").send_keys("125")
        driver.find_element_by_id("totalPoPus").click()
        driver.find_element_by_id("totalPoPus").clear()
        driver.find_element_by_id("totalPoPus").send_keys("523")
        driver.find_element_by_id("tpVillages").click()
        driver.find_element_by_id("tpVillages").clear()
        driver.find_element_by_id("tpVillages").send_keys("25")
        driver.find_element_by_id("tpFamilys").click()
        driver.find_element_by_id("tpFamilys").clear()
        driver.find_element_by_id("tpFamilys").send_keys("80")
        driver.find_element_by_id("tpPoPus").click()
        driver.find_element_by_id("tpPoPus").clear()
        driver.find_element_by_id("tpPoPus").send_keys("250")
        driver.find_element_by_id("hadTpVillages").click()
        driver.find_element_by_id("hadTpVillages").clear()
        driver.find_element_by_id("hadTpVillages").send_keys("26")
        driver.find_element_by_id("hadTpFamilys").click()
        driver.find_element_by_id("hadTpFamilys").clear()
        driver.find_element_by_id("hadTpFamilys").send_keys("80")
        driver.find_element_by_id("hadTpVillages").click()
        driver.find_element_by_id("hadTpVillages").clear()
        driver.find_element_by_id("hadTpVillages").send_keys("25")
        driver.find_element_by_id("hadTpPoPus").click()
        driver.find_element_by_id("hadTpPoPus").clear()
        driver.find_element_by_id("hadTpPoPus").send_keys("250")
        driver.find_element_by_id("returnFamilys").click()
        driver.find_element_by_id("returnFamilys").clear()
        driver.find_element_by_id("returnFamilys").send_keys("0")
        driver.find_element_by_id("returnPoPus").click()
        driver.find_element_by_id("returnPoPus").clear()
        driver.find_element_by_id("returnPoPus").send_keys("0")
        driver.find_element_by_css_selector("div.div-btn").click()
        driver.find_element_by_link_text(u"添加").click()
        driver.find_element_by_css_selector("input[type=\"checkbox\"]").click()
        driver.find_element_by_xpath("//input[@value='610802028006']").click()
        driver.find_element_by_xpath("//input[@value='610802028011']").click()
        driver.find_element_by_xpath("//input[@value='610802028016']").click()
        driver.find_element_by_xpath("//input[@value='610802028021']").click()
        driver.find_element_by_xpath("//input[@value='610802028026']").click()
        driver.find_element_by_xpath("//input[@value='610802028031']").click()
        driver.find_element_by_xpath("//input[@value='610802028002']").click()
        driver.find_element_by_xpath("//input[@value='610802028007']").click()
        driver.find_element_by_xpath("//input[@value='610802028012']").click()
        driver.find_element_by_xpath("//input[@value='610802028017']").click()
        driver.find_element_by_xpath("//input[@value='610802028022']").click()
        driver.find_element_by_xpath("//input[@value='610802028032']").click()
        driver.find_element_by_xpath("//input[@value='610802028027']").click()
        driver.find_element_by_xpath("//input[@value='610802028003']").click()
        driver.find_element_by_id("saveBtns").click()
        driver.find_element_by_id("totalPoorVillages").click()
        driver.find_element_by_link_text(u"添加").click()
        driver.find_element_by_css_selector("div.sm-dialog-close").click()
        driver.find_element_by_id("totalPoorVillages").click()
        driver.find_element_by_id("totalPoorVillages").clear()
        driver.find_element_by_id("totalPoorVillages").send_keys("33")
        driver.find_element_by_id("hadTpVillages").click()
        driver.find_element_by_id("hadTpVillages").clear()
        driver.find_element_by_id("hadTpVillages").send_keys("13")
        driver.find_element_by_id("hadTpFamilys").click()
        driver.find_element_by_id("hadTpVillages").click()
        driver.find_element_by_id("hadTpVillages").clear()
        driver.find_element_by_id("hadTpVillages").send_keys("12")
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[3]").click()
        driver.find_element_by_css_selector("button.back-btn").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[2]").click()
        driver.find_element_by_css_selector("button.back-btn").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确认要删除吗[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确认要删除吗[\s\S]$")
        driver.find_element_by_css_selector("button.back-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
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
