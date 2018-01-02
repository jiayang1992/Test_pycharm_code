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
        driver.find_element_by_id("menu-sm0").click()
        driver.find_element_by_id("second-00").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_css_selector("input.form-btn").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyGroup"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("button.dialog-btn").click()
        print(driver.find_element_by_class_name("n-msg").text)
        driver.find_element_by_name("partyGroupName").clear()
        driver.find_element_by_name("partyGroupName").send_keys(u"茶阳村党支部")
        driver.find_element_by_name("partyGroupCode").clear()
        driver.find_element_by_name("partyGroupCode").send_keys("110002")
        driver.find_element_by_id("companyNameId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectDepartId"))
        driver.find_element_by_id("treeDemo_1_span").click()
        driver.find_element_by_id("treeDemo_1_span").click()
        driver.find_element_by_id("treeDemo_2_check").click()
        # currenceWindow = driver.current_window_handle
        # allhandles = driver.window_handles
        # for handle in allhandles:
        #     if handle != currenceWindow:
        #         driver.switch_to_window(handle)
        #         driver.implicitly_wait(10)

        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyGroup"))
        driver.find_element_by_id("xzAreaNameId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectAreaId"))
        driver.find_element_by_id("treeDemo_1_span").click()
        driver.find_element_by_id("treeDemo_1_switch").click()
        time.sleep(3)
        driver.find_element_by_id("treeDemo_3_span").click()
        driver.find_element_by_id("treeDemo_3_switch").click()
        driver.find_element_by_id("treeDemo_4_span").click()
        driver.find_element_by_id("treeDemo_4_switch").click()
        driver.find_element_by_id("treeDemo_5_span").click()
        driver.find_element_by_id("treeDemo_5_check").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyGroup"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        Select(driver.find_element_by_name("partyRelation")).select_by_visible_text(u"镇")
        Select(driver.find_element_by_name("partyAttachRelation")).select_by_visible_text(u"镇")
        Select(driver.find_element_by_name("compEconomicType")).select_by_visible_text(u"私营经济")
        Select(driver.find_element_by_name("compIndustryType")).select_by_visible_text(u"建筑建材")
        driver.find_element_by_name("contactName").clear()
        driver.find_element_by_name("contactName").send_keys(u"张宇")
        driver.find_element_by_name("contactPhone").clear()
        driver.find_element_by_name("contactPhone").send_keys("15236897525")
        driver.find_element_by_name("groupAddr").clear()
        driver.find_element_by_name("groupAddr").send_keys(u"陕西省榆林市镇川镇")
        driver.find_element_by_name("groupDes").clear()
        driver.find_element_by_name("groupDes").send_keys(u"无")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        time.sleep(5)
        self.assertEqual(u"添加成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_css_selector("input.form-btn").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyGroup"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_1_span").click()
        driver.find_element_by_id("partGroupTree_1_switch").click()
        time.sleep(3)
        driver.find_element_by_id("partGroupTree_33_span").click()
        driver.find_element_by_id("partGroupTree_32_span").click()
        driver.find_element_by_id("partGroupTree_2_span").click()
        driver.find_element_by_id("partGroupTree_3_span").click()
        driver.find_element_by_id("partGroupTree_5_span").click()
        driver.find_element_by_id("partGroupTree_9_span").click()
        driver.find_element_by_id("partGroupTree_1_span").click()
        driver.find_element_by_id("partGroupTree_1_switch").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_link_text(u"下一页").click()
        driver.find_element_by_link_text(u"下一页").click()
        driver.find_element_by_link_text(u"尾页").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'查看')])[2]").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewPartyGroup"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("li > #closeId").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        time.sleep(3)
        driver.find_element_by_xpath(u"(//a[contains(text(),'编辑')])[2]").click()
        time.sleep(3)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyGroup"))
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_link_text(u"尾页").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[2]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此党建机构信息吗[\s\S]$")
        driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[2]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此党建机构信息吗[\s\S]$")
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        time.sleep(3)
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
