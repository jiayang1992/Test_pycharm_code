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
        driver.find_element_by_css_selector("li.unnum0").click()
        driver.find_element_by_id("menu-sm1").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_css_selector("img.cursor").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='atrDialogIframe_selectDepartId']"))
        driver.find_element_by_id("partGroupTree_1_switch").click()
        time.sleep(4)
        driver.find_element_by_id("partGroupTree_41_switch").click()
        time.sleep(4)
        driver.find_element_by_id("partGroupTree_48_switch").click()
        time.sleep(4)
        driver.find_element_by_id("partGroupTree_49_check").click()
        time.sleep(4)
        driver.find_element_by_css_selector("button.dialog-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))

        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"测试")
        Select(driver.find_element_by_id("publicSTypeId")).select_by_visible_text(u"班子建设")
        driver.find_element_by_name("publicRange").clear()
        driver.find_element_by_name("publicRange").send_keys(u"全部")
        driver.find_element_by_id("startDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_css_selector("div.navImg.NavImgll > a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[5]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("endDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[7]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_class_name("swfupload").click()
        os.system("upload_document.exe")
        time.sleep(4)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/form/table/tbody/tr[11]/td[2]/div/div[2]/iframe"))
        driver.find_element_by_css_selector("body.ke-content").send_keys("测试")
        time.sleep(3)
        # js_bottom = "var drag_to_bottom = document.body.scrollTop = 10000"
        # driver.execute_script(js_bottom)
        driver.switch_to_default_content()
        js_bottom = "var drag_to_bottom = document.body.scrollTop=10000 "
        driver.execute_script(js_bottom)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        js_bottom = "var drag_to_bottom = document.body.scrollTop=10000 "
        driver.execute_script(js_bottom)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("button.save-btn").click()

        # driver.find_element_by_name("dosubmit").click()
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_id("villageNameId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("img.cursor").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='atrDialogIframe_selectDepartId']"))
        driver.find_element_by_id("partGroupTree_1_switch").click()
        time.sleep(4)
        driver.find_element_by_id("partGroupTree_3_switch").click()
        time.sleep(4)
        driver.find_element_by_id("partGroupTree_4_check").click()
        time.sleep(4)
        time.sleep(4)
        driver.find_element_by_css_selector("button.dialog-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_css_selector("input.back-btn").click()

        # driver.find_element_by_id("startDate").click()
        # driver.switch_to_default_content()
        # driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        # driver.find_element_by_css_selector("div.navImg.NavImgll > a").click()
        # driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[5]").click()
        # time.sleep(4)
        # driver.switch_to_default_content()
        # driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # driver.find_element_by_id("endDate").click()
        # driver.switch_to_default_content()
        # driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        # driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[7]").click()
        # driver.find_element_by_css_selector("button.save-btn").click()
        # driver.switch_to_default_content()
        # driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"测试")
        time.sleep(4)
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"查看").click()
        driver.find_element_by_link_text(u"下载").click()
        driver.find_element_by_name("dosubmit").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_css_selector("img.cursor").click()
        driver.switch_to_frame(driver.find_element_by_xpath("//*[@id='atrDialogIframe_selectDepartId']"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("partGroupTree_1_switch").click()
        time.sleep(4)
        driver.find_element_by_id("partGroupTree_28_switch").click()
        time.sleep(4)
        driver.find_element_by_id("partGroupTree_29_switch").click()
        time.sleep(4)
        driver.find_element_by_id("partGroupTree_30_check").click()
        time.sleep(4)
        driver.find_element_by_css_selector("button.dialog-btn").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"测试01")
        Select(driver.find_element_by_id("publicTypeId")).select_by_visible_text(u"村务公开")
        Select(driver.find_element_by_id("publicSTypeId")).select_by_visible_text(u"宅基地审批")
        driver.find_element_by_css_selector("button.save-btn").click()
        print("编辑成功")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"测试")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以新增村务名称'测试'搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_link_text(u"查看").click()
        driver.find_element_by_name("dosubmit").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"测试")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以新增村务名称'测试'搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"测试")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("以新增村务名称'测试'搜索，搜索到 %d 条结果" % int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
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
