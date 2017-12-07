# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class RoleManager(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path,chrome_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
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
        driver.find_element_by_css_selector("li.unnum2").click()
        driver.find_element_by_id("second-00").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_id("roleName").clear()
        time.sleep(2)
        driver.find_element_by_id("roleName").send_keys("jiayang")
        driver.find_element_by_id("roleDesc").clear()
        driver.find_element_by_id("roleDesc").send_keys("tester")
        Select(driver.find_element_by_id("role_dbPrivilege")).select_by_visible_text("select,insert,update,delete")
        time.sleep(2)
        driver.find_element_by_id("ywxrole").click()
        driver.find_element_by_id("operaterole").click()
        driver.find_element_by_id("treeDemo2_1_switch").click()
        driver.find_element_by_id("treeDemo2_1_switch").click()
        driver.find_element_by_id("treeDemo2_1_check").click()

        time.sleep(7)
        driver.find_element_by_id("treeDemo2_4_switch").click()
        driver.find_element_by_id("treeDemo2_5_check").click()
        driver.find_element_by_id("treeDemo2_4_switch").click()

        time.sleep(7)
        driver.find_element_by_id("treeDemo2_24_switch").click()
        driver.find_element_by_id("treeDemo2_25_switch").click()
        driver.find_element_by_id("treeDemo2_24_check").click()
        driver.find_element_by_id("treeDemo2_24_switch").click()

        driver.find_element_by_id("treeDemo2_28_switch").click()
        driver.find_element_by_id("treeDemo2_28_check").click()
        driver.find_element_by_id("treeDemo2_28_switch").click()

        driver.find_element_by_id("treeDemo2_68_switch").click()
        driver.find_element_by_id("treeDemo2_68_check").click()
        driver.find_element_by_id("treeDemo2_68_switch").click()
        driver.find_element_by_class_name("save-btn").click()
        time.sleep(3)
        self.assertEqual(u"新增成功!", self.close_alert_and_get_its_text())
        driver.find_element_by_id("roleName").clear()
        driver.find_element_by_id("roleName").send_keys("jiayang")
        Select(driver.find_element_by_id("dstatus")).select_by_visible_text(u"启用")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"编辑").click()
        time.sleep(2)
        driver.find_element_by_css_selector("button.back-btn").click()
        driver.find_element_by_id("roleName").clear()
        driver.find_element_by_id("roleName").send_keys("jiayang")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"编辑").click()
        time.sleep(2)
        driver.find_element_by_css_selector("button.back-btn").click()
        driver.find_element_by_id("roleName").clear()
        driver.find_element_by_id("roleName").send_keys("jiayang")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("roleName").clear()
        driver.find_element_by_id("roleName").send_keys("jiayang")
        Select(driver.find_element_by_id("dstatus")).select_by_visible_text(u"启用")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_link_text(u"下一页").click()
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_link_text(u"首页").click()
        driver.find_element_by_link_text(u"尾页").click()
        driver.find_element_by_link_text(u"上一页").click()
        driver.find_element_by_id("topageNo").clear()
        driver.find_element_by_id("topageNo").send_keys("2")
        driver.find_element_by_css_selector("input.page-btn").click()
        driver.find_element_by_id("roleName").clear()
        driver.find_element_by_id("roleName").send_keys("jiayang")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^删除后将无法恢复,确定要删除吗[\s\S]$")
        driver.find_element_by_id("roleName").clear()
        driver.find_element_by_id("roleName").send_keys("jiayang")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
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
