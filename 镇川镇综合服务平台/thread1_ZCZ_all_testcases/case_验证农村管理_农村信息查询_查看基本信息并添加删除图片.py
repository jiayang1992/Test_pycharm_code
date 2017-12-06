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
        self.base_url = "http://101.201.41.228:7006/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case(self):
        driver = self.driver
        driver.get(self.base_url + "/ylsn1.5/manage/user/login")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum0").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_id("villageAttriId")).select_by_visible_text(u"贫困村")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("610802028009").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # 将滚动条拖至最底下
        # js_bottom = "var drag_to_bottom = document.documentElement.scrollTop=10000 "
        # driver.execute_script(js_bottom)
        # time.sleep(2)
        #
        # js_top = "var drag_to_top = document.documentElement.scrollTop=0 "
        # driver.execute_script(js_top)
        # time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='atrDialogIframe_villageId']"))
        js_bottom = "var drag_to_bottom = document.body.scrollTop=10000 "
        driver.execute_script(js_bottom)
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='imgFormt16']/div[2]/span/div[3]/div[2]/div").click()
        os.system("uploadpicture.exe")

        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.execute_script(js_bottom)
        driver.find_element_by_name("imgNames").clear()
        #driver.find_element_by_id("1512444733475937").clear()
        driver.find_element_by_name("imgNames").send_keys(u"测试")
        driver.execute_script(js_bottom)
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.execute_script(js_bottom)
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.execute_script(js_bottom)
        driver.find_element_by_class_name("save-btn").click()


        # driver.execute_script(js_bottom)
        # driver.find_element_by_link_text("删除").click()
        # self.assertEqual(u"删除后将无法恢复，确定要删除吗", self.close_alert_and_get_its_text())
        # self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        # driver.find_element_by_css_selector("button.save-btn").click()


        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("closeId").click()
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
