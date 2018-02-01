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
        driver.find_element_by_id("menu-sm3").click()
        driver.find_element_by_id("second-31").click()
        driver.find_element_by_css_selector("#level-31 > ul > #menuli11").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("fid0").click()
            # driver.find_element_by_id("setHelpMethods").click()
            # driver.find_element_by_link_text(u"移除").click()
            # driver.find_element_by_link_text(u"添加").click()
            # driver.find_element_by_link_text(u"一键重置").click()
            # driver.find_element_by_link_text(u"添加").click()
            # # element0 = driver.find_elements_by_xpath("/html/body/div[11]/table/tbody/tr[2]/td[4]/div/table/tbody/tr[12]/td[2]/span")
            # # for ele0 in element0:
            # #     if ele0.is_displayed():
            # #         ele0.click()
            # # time.sleep(3)
            # # # driver.find_element_by_xpath("/html/body/div[11]/table/tbody/tr[2]/td[4]/div/table/tbody/tr[12]/td[2]/span").click()
            # # # time.sleep(3)
            # # # driver.find_element_by_xpath("/html/body/div[11]/table/tbody/tr[2]/td[4]/div/table/tbody/tr[12]/td[2]/span").click()
            # # driver.find_element_by_xpath("//*[@id='7000101']").click()
            # driver.find_element_by_xpath("//*[@id='10000101']").click()
            # driver.find_element_by_xpath("//*[@id='1474967387187']").click()
            # # driver.find_element_by_xpath("/html/body/div[11]/table/tbody/tr[2]/td[4]/div/table/tbody/tr[18]/td[2]/span").click()
            # # driver.find_element_by_xpath("//*[@id='1502356175468321']").click()
            # driver.find_element_by_link_text(u"保存设置").click()
            # self.assertEqual(u"设置成功!", self.close_alert_and_get_its_text())
            # driver.find_element_by_id("setHelpMethods").click()
            # self.assertEqual(u"请先选择要操作的内容！", self.close_alert_and_get_its_text())
            # driver.find_element_by_id("fid0").click()
        driver.find_element_by_id("setHelpMethods").click()
        driver.find_element_by_css_selector("div.sm-dialog-close").click()
        driver.find_element_by_link_text(u"措施变更").click()
        driver.find_element_by_css_selector("#operateMethod > #1502356175468321 > a").click()
        driver.find_element_by_link_text(u"一键添加").click()
        driver.find_element_by_css_selector("#1516689593264893 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #1474967387187 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #1474967407850 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #1474967310818 > a").click()
        driver.find_element_by_css_selector("#1502355248504431 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #1474967370902 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #10000101 > a").click()
        driver.find_element_by_css_selector("#1502356209903875 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #1502356175468321 > a").click()
        driver.find_element_by_css_selector("#1502356258363375 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #1474967413152 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #1474967395963 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #7000101 > a").click()
        driver.find_element_by_css_selector("#1498008053294125 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #1474967380047").click()
        driver.find_element_by_css_selector("#operateMethod > #1474967380047 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #6000102 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #6000101 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #1481784093792153").click()
        driver.find_element_by_css_selector("#operateMethod > #1481784093792153 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #5000103").click()
        driver.find_element_by_css_selector("#operateMethod > #1474967402153 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #5000103 > a").click()
        driver.find_element_by_css_selector("#operateMethod > #5000102 > a").click()
        driver.find_element_by_link_text(u"保存更改").click()
        self.assertEqual(u"设置成功!", self.close_alert_and_get_its_text())
        driver.find_element_by_id("3117030423").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_css_selector("input.dialog-btn").click()
        driver.find_element_by_css_selector("input.dialog-btn").click()
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("3117030423").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_id("switch-big5").click()
        driver.find_element_by_id("switch-big6").click()
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
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
