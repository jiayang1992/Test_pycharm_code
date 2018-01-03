# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

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
        driver.find_element_by_id("menu-sm1").click()
        driver.find_element_by_id("second-10").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_xpath("//*[@id='partyFlowFormId']/ul/li[2]/input").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyFlowId"))
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("input.form-btn").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyFlowId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("img").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyFlowId"))
        driver.find_element_by_css_selector("img").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpTodayInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyFlowId"))
        driver.find_element_by_css_selector("img.cursor").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectMemberId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_link_text(u"下一页").click()
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.find_element_by_xpath("//*[@id='partyMemberFormId']/div[2]/table/tbody/tr[6]/td[1]/label/input").click()
        driver.find_element_by_css_selector("input.save-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyFlowId"))

        #driver.find_element_by_id("subId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        time.sleep(5)
        driver.find_element_by_id("cursorId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectGroupId"))
        driver.find_element_by_id("treeDemo_1_switch").click()
        driver.find_element_by_id("treeDemo_3_check").click()
        driver.find_element_by_css_selector("button.dialog-btn").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyFlowId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_name("flowReason").clear()
        driver.find_element_by_name("flowReason").send_keys(u"结婚")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        time.sleep(3)
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_xpath(u"(//a[contains(text(),'查看')])[8]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewPartyWorkId"))
        driver.find_element_by_css_selector("li > #closeId").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        time.sleep(3)
        driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[8]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyWorkId"))
        driver.find_element_by_css_selector("img").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpTodayInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyWorkId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("button.dialog-btn").click()
        driver.find_element_by_id("cursorId").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectGroupId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("treeDemo_1_switch").click()
        time.sleep(3)
        driver.find_element_by_id("treeDemo_4_check").click()
        driver.find_element_by_css_selector("button.dialog-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyWorkId"))
        Select(driver.find_element_by_name("pType")).select_by_visible_text(u"跨地域")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"修改成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        self.accept_next_alert = False
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[8]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此流转情况信息吗[\s\S]$")
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[8]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此流转情况信息吗[\s\S]$")
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
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
