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
        driver.find_element_by_id("menu-sm4").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        time.sleep(6)
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        value1 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("共有%d条缴费记录" % int(value1))
        driver.find_element_by_css_selector("input.form-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        driver.find_element_by_css_selector("img.cursor").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectMemberId"))
        driver.find_element_by_name("rd").click()
        driver.find_element_by_css_selector("input.save-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        driver.find_element_by_id("payYyyymmStart").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[6]/td").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        driver.find_element_by_id("payYyyymmEnd").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[6]/td").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("payAmountId").clear()
        driver.find_element_by_id("payAmountId").send_keys("55")
        driver.find_element_by_name("exitReason").clear()
        driver.find_element_by_name("exitReason").send_keys(u"无")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_css_selector("input.form-btn").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"必须选择人员！", self.close_alert_and_get_its_text())
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        driver.find_element_by_css_selector("img.cursor").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectMemberId"))
        driver.find_element_by_xpath("//*[@id='partyMemberFormId']/div[2]/table/tbody/tr[5]/td[1]/label/input").click()
        driver.find_element_by_css_selector("input.save-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"开始时间与结束时间不能为空且截止时间要大于起始时间", self.close_alert_and_get_its_text())
        driver.find_element_by_id("payYyyymmStart").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[6]/td").click()

        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        driver.find_element_by_id("payYyyymmEnd").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[6]/td").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"开始时间与结束时间不能为空且截止时间要大于起始时间", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]

        driver.find_element_by_id("payYyyymmStart").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("dpClearInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        driver.find_element_by_id("payYyyymmStart").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[6]/td").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        driver.find_element_by_id("payYyyymmEnd").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[6]/td").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyDuesId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("payAmountId").clear()
        driver.find_element_by_id("payAmountId").send_keys("35")
        driver.find_element_by_name("exitReason").clear()
        driver.find_element_by_name("exitReason").send_keys(u"无")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        value2 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("添加两条缴费记录后，现在共有%d条缴费记录" % int(value2))
        driver.find_element_by_xpath("//*[@id='partyDuesFormId']/div[3]/div/a[7]").click()
        #查看
        driver.find_element_by_xpath("//*[@id='partyDuesFormId']/div[2]/table/tbody/tr[6]/td[8]/a[1]").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewPartyDuesId"))
        element0 = driver.find_elements_by_id("closeId")
        for ele0 in element0:
            if ele0.is_displayed():
                ele0.click()
        # driver.find_element_by_id("closeId").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        #编辑
        # driver.find_element_by_xpath("//*[@id='partyDuesFormId']/div[3]/div/a[7]").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='partyDuesFormId']/div[2]/table/tbody/tr[6]/td[8]/a[2]").click()
        time.sleep(5)
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyDuesId"))
        element1 = driver.find_elements_by_id("closeId")
        for ele1 in element1:
            if ele1.is_displayed():
                ele1.click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        #编辑
        # driver.find_element_by_xpath("//*[@id='partyDuesFormId']/div[3]/div/a[7]").click()
        driver.find_element_by_xpath("//*[@id='partyDuesFormId']/div[2]/table/tbody/tr[6]/td[8]/a[2]").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyDuesId"))
        driver.find_element_by_id("payAmountId").clear()
        driver.find_element_by_id("payAmountId").send_keys("52")
        driver.find_element_by_class_name("dialog-btn").click()
        self.assertEqual(u"修改成功！",self.close_alert_and_get_its_text())
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_xpath("//*[@id='partyDuesFormId']/div[3]/div/a[7]").click()

        self.accept_next_alert = False
        driver.find_element_by_xpath(u"//*[@id='partyDuesFormId']/div[2]/table/tbody/tr[6]/td[8]/a[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此党费缴纳记录信息吗?[\s\S]$")
        driver.find_element_by_xpath(u"//*[@id='partyDuesFormId']/div[2]/table/tbody/tr[6]/td[8]/a[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此党费缴纳记录信息吗?[\s\S]$")
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("//*[@id='partyDuesFormId']/div[3]/div/a[1]").click()
        time.sleep(5)
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
