# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
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
        driver.find_element_by_id("menu-sm3").click()
        driver.find_element_by_id("second-30").click()
        # menu = driver.find_element_by_id("second-30").find_element_by_id("menuli00")
        # ActionChains(driver).move_to_element(menu).perform()
        element0 = driver.find_elements_by_id("menuli00")
        for ele0 in element0:
            if ele0.is_displayed():
                ele0.click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("toAddBtn").click()
        # driver.find_element_by_id("parentselect").click()
        # Select(driver.find_element_by_id("parentselect")).select_by_visible_text(u"专项扶贫")
        # driver.find_element_by_css_selector("option[value=\"1474962427651\"]").click()
        driver.find_element_by_id("measureName").clear()
        driver.find_element_by_id("measureName").send_keys(u"实践")
        driver.find_element_by_id("isUsed").click()
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_name("dosubmit").click()
        # driver.find_element_by_css_selector("span.treegrid-expander.treegrid-expander-collapsed").click()
        # driver.find_element_by_xpath("//table[@id='treegrid']/tbody/tr[3]/td[2]").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[2]").click()
        driver.find_element_by_name("dosubmit").click()
        # driver.find_element_by_css_selector("span.treegrid-expander.treegrid-expander-collapsed").click()
        #在父级下添加子级菜单
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_id("parentselect").click()
        Select(driver.find_element_by_id("parentselect")).select_by_value("1497510670873739")
        driver.find_element_by_id("measureName").clear()
        driver.find_element_by_id("measureName").send_keys(u"管理基地费用")
        driver.find_element_by_id("isUsed").click()
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_css_selector("span.treegrid-expander.treegrid-expander-collapsed").click()
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td[2]/span").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/table/tbody/tr[2]/td[2]/span").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[2]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[2]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
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
