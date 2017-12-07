# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class DeleteAllFailToImportData(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    # def is_element_exist(css):
    #     driver = css.driver
    #     s = driver.find_element_by_css_selector(css_selector=css)
    #     if len(s) == 0:
    #         print("没有导入失败的数据：%s"%css)
    #         return False
    #     elif len(s) == 1:
    #         return True
    #     else:
    #         print("导入失败的数据为:%s"%(len(s),css))
    #         return False
    # if is_element_exist("input.ace"):

    def test_(self):
        driver = self.driver
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
        driver.find_element_by_xpath("//div[@onclick=\"window.location.href='selectRemainList';\"]").click()
        driver.find_element_by_id("firstCheckbox").click()
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^删除后将无法恢复,确定要删除吗[\s\S]$")
        time.sleep(3)
        self.assertEqual(u"删除成功", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("div.fl-l.lead-btn").click()
        driver.find_element_by_xpath("//div[@onclick=\"window.location.href='selectRemainList';\"]").click()
        driver.find_element_by_css_selector("div.fl-l.lead-btn").click()
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"退出").click()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("111111")
    
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
