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
        self.base_url = "http://101.201.41.228:7006/ylsn1.5/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/ylsn1.5/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum2").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.find_element_by_id("menu-sm1").click()
        driver.find_element_by_id("second-10").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("button.edit-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='atrDialogIframe_selectCadre']"))
        driver.find_element_by_id("treeDemo_1_span").click()
        driver.find_element_by_id("treeDemo_1_switch").click()
        time.sleep(3)
        driver.find_element_by_id("treeDemo_5_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
        time.sleep(3)
        driver.find_element_by_css_selector("button.edit-btn").click()
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='atrDialogIframe_selectCadre']"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("treeDemo_1_span").click()
        driver.find_element_by_id("treeDemo_1_switch").click()
        time.sleep(3)
        driver.find_element_by_id("treeDemo_5_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"刘")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"刘阳")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("telPhone").clear()
        driver.find_element_by_id("telPhone").send_keys("182")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("telPhone").clear()
        driver.find_element_by_id("telPhone").send_keys("18291202239")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("telPhone").clear()
        driver.find_element_by_id("telPhone").send_keys("18291202239")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_id("dutyLevel")).select_by_visible_text(u"科员级")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("ids").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_class_name(" aui_state_highlight").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
        time.sleep(3)
        driver.find_element_by_id("treeDemo_1_switch").click()
        driver.find_element_by_id("treeDemo_12_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"刘阳")
        driver.find_element_by_css_selector("button.form-btn").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"查看").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewPartyMemberId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("closeId").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"配置考勤区域").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_mapId"))
        driver.find_element_by_css_selector("button.edit-btn").click()
        driver.find_element_by_id("startBtn").click()
        driver.find_element_by_id("name").send_keys("老庄")
        #js = "$('input[id=map]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
        js = "$('input[id=map]').removeAttr('readonly')"
        driver.execute_script(js)
        driver.find_element_by_id("map").send_keys("109.700052,38.240727;")
        #点击清除按钮
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]/button[2]").click()
        time.sleep(3)

        js = "$('input[id=map]').removeAttr('readonly')"  # 4.jQuery，设置为空（同3）
        driver.execute_script(js)
        driver.find_element_by_id("map").send_keys("109.700052,38.240727;")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("closeId").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"配置考勤区域").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_mapId"))
        driver.find_element_by_link_text(u"查看").click()
        time.sleep(3)
        driver.find_element_by_class_name("edit-btn").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]/button[2]").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("墩梁")
        driver.find_element_by_id("map").send_keys("109.749423,38.493758;")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(3)
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("closeId").click()
        time.sleep(3)
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"刘阳")
        driver.find_element_by_css_selector("button.form-btn").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^删除后将无法恢复,确定要删除吗[\s\S]$")
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^删除后将无法恢复,确定要删除吗[\s\S]$")
        time.sleep(3)
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"刘阳")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("resetBtn").click()
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
