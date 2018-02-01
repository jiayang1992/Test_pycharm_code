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
        driver.find_element_by_id("userNameCopy").click()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").click()
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("1")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum9").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("treeDemo_7_span").click()
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_css_selector("ul.form-ul > li > input.form-btn").click()
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"测试")
        driver.find_element_by_id("noter").click()
        driver.find_element_by_id("noter").clear()
        driver.find_element_by_id("noter").send_keys(u"李四")
        driver.find_element_by_id("business1").click()
        Select(driver.find_element_by_id("business1")).select_by_visible_text(u"产业发展")
        driver.find_element_by_css_selector("option[value=\"1503630518351614\"]").click()
        time.sleep(3)
        driver.find_element_by_id("business2").click()
        Select(driver.find_element_by_id("business2")).select_by_visible_text(u"文化旅游")
        driver.find_element_by_xpath("(//option[@name='twoLv'])[2]").click()
        driver.find_element_by_id("startTime").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("endTime").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_name("content").click()
        driver.find_element_by_name("content").clear()
        driver.find_element_by_name("content").send_keys(u"测试")
        driver.find_element_by_class_name("swfupload").click()
        os.system("uploadpicture.exe")
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"你确定删除此附件吗？", self.close_alert_and_get_its_text())
        self.accept_next_alert = True
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"你确定删除此附件吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_class_name("swfupload").click()
        os.system("uploadpicture.exe")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        driver.find_element_by_link_text(u"查看").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewthreepartyId"))
        driver.find_element_by_link_text(u"点击下载").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("closeId").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updthreepartyId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("business1").click()
        Select(driver.find_element_by_id("business1")).select_by_visible_text(u"产业发展")
        driver.find_element_by_css_selector("option[value=\"1503630518351614\"]").click()
        driver.find_element_by_id("business2").click()
        Select(driver.find_element_by_id("business2")).select_by_visible_text(u"文化旅游")
        driver.find_element_by_xpath("(//option[@name='twoLv'])[2]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("startTime").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("endTime").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此信息吗[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此信息吗[\s\S]$")
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
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
