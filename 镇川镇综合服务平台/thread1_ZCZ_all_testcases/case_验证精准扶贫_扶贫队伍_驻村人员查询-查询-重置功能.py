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
        driver.find_element_by_id("menu-sm2").click()
        driver.find_element_by_id("second-21").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("departName").click()
        driver.find_element_by_id("departName").clear()
        driver.find_element_by_id("departName").send_keys(u"咸阳师范学院")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以部门名称'咸阳师范学院'查询到%d条结果"%int(value))
        driver.find_element_by_link_text(u"查看").click()
        driver.find_element_by_css_selector("button.back-btn").click()
        driver.find_element_by_css_selector("li.formli").click()
        driver.find_element_by_id("departName").click()
        driver.find_element_by_id("departName").clear()
        driver.find_element_by_id("departName").send_keys(u"咸阳师范学院")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("depPid").click()
        Select(driver.find_element_by_name("depPid")).select_by_visible_text(u"省级部门")
        driver.find_element_by_css_selector("option[value=\"1001\"]").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以'省级部门'查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("depPid").click()
        Select(driver.find_element_by_name("depPid")).select_by_visible_text(u"市级部门")
        driver.find_element_by_css_selector("option[value=\"1002\"]").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以'市级部门'查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("depPid").click()
        Select(driver.find_element_by_name("depPid")).select_by_visible_text(u"县级部门")
        driver.find_element_by_css_selector("option[value=\"1003\"]").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以'县级部门'查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("depPid").click()
        Select(driver.find_element_by_name("depPid")).select_by_visible_text(u"乡镇部门")
        driver.find_element_by_css_selector("option[value=\"1004\"]").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以'乡镇部门'查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("depPid").click()
        Select(driver.find_element_by_name("depPid")).select_by_visible_text(u"村委会")
        driver.find_element_by_css_selector("option[value=\"1005\"]").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以'村委会'查询到%d条结果" % int(value))
        driver.find_element_by_link_text(u"查看").click()
        driver.find_element_by_css_selector("button.back-btn").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"张")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以关键字'张'查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("telephone").click()
        driver.find_element_by_id("telephone").clear()
        driver.find_element_by_id("telephone").send_keys("132")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以联系电话关键字'132'查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("idCard").click()
        driver.find_element_by_id("idCard").clear()
        driver.find_element_by_id("idCard").send_keys("61")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以身份证号关键字'61'查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("idCard").click()
        driver.find_element_by_id("idCard").clear()
        driver.find_element_by_id("idCard").send_keys("2")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以身份证号关键字'2'查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("isDelete").click()
        driver.find_element_by_id("isDelete").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("isDelete").click()
        Select(driver.find_element_by_id("isDelete")).select_by_visible_text(u"已删除")
        driver.find_element_by_css_selector("option[value=\"y\"]").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以人员状态'已删除'查询到%d条结果" % int(value))
        driver.find_element_by_id("isDelete").click()
        Select(driver.find_element_by_id("isDelete")).select_by_visible_text(u"正常")
        driver.find_element_by_css_selector("option[value=\"n\"]").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以人员状态'正常'查询到%d条结果" % int(value))
        driver.find_element_by_id("resetBtn").click()
        # driver.find_element_by_id("name").click()
        # driver.find_element_by_id("name").clear()
        # driver.find_element_by_id("name").send_keys(u"张")
        # driver.find_element_by_css_selector("button.form-btn").click()
        # driver.find_element_by_name("ids").click()
        # driver.find_element_by_css_selector("input.save-btn").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        # driver.find_element_by_id("treeDemo_3_check").click()
        # # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # self.assertEqual(u"已成功提取至平台层!", self.close_alert_and_get_its_text())
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
