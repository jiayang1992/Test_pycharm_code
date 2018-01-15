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
        driver.find_element_by_id("menu-sm6").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_1_a").click()
        driver.find_element_by_id("partGroupTree_1_switch").click()
        driver.find_element_by_id("partGroupTree_2_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_css_selector("input.form-btn").click()
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("Test")
        driver.find_element_by_id("address").clear()
        driver.find_element_by_id("address").send_keys(u"榆林")
        driver.find_element_by_id("programme").clear()
        driver.find_element_by_id("programme").send_keys(u"张三")
        driver.find_element_by_id("meetingDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[4]/td[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        Select(driver.find_element_by_name("type")).select_by_visible_text(u"党小组会议")
        driver.find_element_by_name("actualNumber").clear()
        driver.find_element_by_name("actualNumber").send_keys("41")
        driver.find_element_by_name("meetingTime").clear()
        driver.find_element_by_name("meetingTime").send_keys("120")
        driver.find_element_by_name("recordName").clear()
        driver.find_element_by_name("recordName").send_keys(u"李四")
        driver.find_element_by_name("content").clear()
        driver.find_element_by_name("content").send_keys(u"无")
        driver.find_element_by_class_name("swfupload").click()
        os.system("uploadpicture.exe")
        time.sleep(3)
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"你确定删除此附件吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"你确定删除此附件吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("button.dialog-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_1_span").click()
        driver.find_element_by_id("partGroupTree_1_span").click()
        driver.find_element_by_id("partGroupTree_2_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("Test")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("查询到%d条结果"%int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        value4 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("重置后有%d条结果" % int(value4))
        if int(value4) < 1:
            print("重置成功")
        else:
            print("重置失败")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("startDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("endDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[4]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_css_selector("button.form-btn").click()
        value1 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("查询到%d条结果" % int(value1))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        value2 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("重置后有%d条结果" % int(value2))
        if int(value2) < 1:
            print("重置成功")
        else:
            print("重置失败")
        driver.find_element_by_link_text(u"查看").click()
        # driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewthreepartyId"))
        element0 = driver.find_elements_by_xpath("//*[@id='closeId']")
        for ele0 in element0:
            if ele0.is_displayed():
                ele0.click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        time.sleep(3)
        driver.find_element_by_link_text(u"编辑").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updthreepartyId"))
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        time.sleep(3)
        driver.find_element_by_link_text(u"编辑").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updthreepartyId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("button.dialog-btn.date-sava-Vaild").click()
        self.assertEqual(u"修改成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_2_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此会议信息吗[\s\S]$")
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此会议信息吗[\s\S]$")
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_2_span").click()
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        value5 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("删除一条会议记录后还有%d条结果" % int(value5))
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
