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
        driver.find_element_by_css_selector("li.unnum2").click()
        driver.find_element_by_id("menu-sm1").click()
        driver.find_element_by_id("menu-sm2").click()
        driver.find_element_by_id("second-20").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("test")
        Select(driver.find_element_by_name("taskType")).select_by_visible_text(u"党建任务")
        driver.find_element_by_id("content").clear()
        driver.find_element_by_id("content").send_keys("test")
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        time.sleep(3)
        driver.find_element_by_id("fileupload").click()
        os.system("uploadpicture.exe")
        time.sleep(5)
            # self.accept_next_alert = False
            # # element0 = driver.find_elements_by_link_text("删除")
            # # for ele0 in element0:
            # #     if ele0.is_displayed():
            # #         ele0.click()
            # driver.find_element_by_link_text("删除").click()
            # self.assertEqual(u"你确定删除此附件吗？", self.close_alert_and_get_its_text())
            #
            # driver.find_element_by_link_text("删除").click()
            # # element0 = driver.find_elements_by_link_text("删除")
            # # for ele0 in element0:
            # #     if ele0.is_displayed():
            # #         ele0.click()
            # self.assertEqual(u"你确定删除此附件吗？", self.close_alert_and_get_its_text())
            # self.assertEqual(u"删除成功", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_id("startDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[6]").click()
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("endDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[7]").click()
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("button.form-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectCadre"))
        driver.find_element_by_id("treeDemo_1_span").click()
        driver.find_element_by_id("treeDemo_1_switch").click()
        driver.find_element_by_id("treeDemo_3_span").click()
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//*[@id='firstCheckbox']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        time.sleep(2)
        driver.find_element_by_class_name(" aui_state_highlight").click()
        # driver.find_element_by_class_name(" aui_state_highlight").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        time.sleep(3)
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectCadre"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"周")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("firstCheckbox").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("button.aui_state_highlight").click()
        driver.find_element_by_css_selector("button.aui_state_highlight").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectCadre"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"李")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_xpath("(//input[@id='firstCheckbox'])[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("button.aui_state_highlight").click()
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='myform']/div/button[1]").click()
        driver.find_element_by_link_text(u"修改").click()
        driver.find_element_by_xpath("//button[@onclick='return submits()']").click()
        driver.find_element_by_link_text(u"修改").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_link_text(u"查看").click()
        driver.find_element_by_id("resetBtn").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^删除后将无法恢复,确定要删除吗[\s\S]$")
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^删除后将无法恢复,确定要删除吗[\s\S]$")
        time.sleep(3)
        self.assertEqual(u"删除成功", self.close_alert_and_get_its_text())
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys("test")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("startDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("startDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("endDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        #查询
        driver.find_element_by_xpath("//*[@id='queryForm']/ul/li[4]/button").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        if value == '0':
            print("点击查询按钮，查询失败")
        else:
            print("按时间范围查询到%d条结果"%int(value))
        #重置
        driver.find_element_by_id("resetBtn").click()
        value1 = driver.find_element_by_id("totalNum").get_attribute("value")
        if value1 == '0':
            print("点击重置按钮，重置失败")
        else:
            print("点击重置按钮后有%d条任务" % int(value1))
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
