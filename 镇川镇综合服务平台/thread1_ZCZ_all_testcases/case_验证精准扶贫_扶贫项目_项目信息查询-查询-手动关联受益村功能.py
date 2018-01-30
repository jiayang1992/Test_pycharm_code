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
        driver.find_element_by_css_selector("li.unnum4").click()
        driver.find_element_by_id("menu-sm4").click()
        driver.find_element_by_id("menu-sm6").click()
        driver.find_element_by_id("second-60").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("villageId").click()
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        driver.find_element_by_css_selector("option[value=\"610802028001\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("projectType").click()
        Select(driver.find_element_by_name("projectType")).select_by_visible_text(u"产业扶贫")
        driver.find_element_by_css_selector("option[value=\"40\"]").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"产业项目")
        driver.find_element_by_css_selector("option[value=\"401\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目申请")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"20\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("isExistFamilys").click()
        Select(driver.find_element_by_name("isExistFamilys")).select_by_visible_text(u"存在")
        driver.find_element_by_css_selector("option[value=\"1\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目支付")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"70\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目检查")
        driver.find_element_by_css_selector("option[value=\"60\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目完成")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"50\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目验收")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"40\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目审核并实施")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"30\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目申请")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"20\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目新建")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"10\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("getInfoBtn").click()
        driver.find_element_by_id("100000192844107").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_projectId"))
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("closeId").click()
        time.sleep(5)
        driver.find_element_by_link_text(u"手动关联受益村").click()
        driver.find_element_by_link_text(u"选择").click()
        driver.find_element_by_link_text("镇川镇").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/div/div[3]/div[3]/ul/li[1]/input").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/div/div[3]/div[3]/ul/li[2]/input").click()
        driver.find_element_by_id("allId").click()
        driver.find_element_by_id("allNoneId").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/div/div[3]/div[3]/ul/li[3]/input").click()
        driver.find_element_by_xpath("/html/body/form/div[1]/div/div[3]/div[3]/ul/li[4]/input").click()
        driver.find_element_by_id("confirmBtn").click()
        # time.sleep(3)
        # self.assertEqual(u"保存成功!", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"选择").click()
        driver.find_element_by_link_text("镇川镇").click()
        driver.find_element_by_id("backId").click()
        driver.find_element_by_id("closeBtn").click()
        driver.find_element_by_id("saveBtn").click()
        time.sleep(5)
        driver.find_element_by_link_text(u"手动关联受益村").click()
        driver.find_element_by_id("backBtn").click()
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
