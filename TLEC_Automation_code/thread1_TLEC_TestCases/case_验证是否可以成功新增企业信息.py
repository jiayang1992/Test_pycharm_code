# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class Add_Enterprise_Info(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.maximize_window()
        driver.find_element_by_css_selector("li.unnum0").click()
        driver.find_element_by_id("menu-sm0").click()
        time.sleep(3)
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("add").click()
        driver.find_element_by_name("enterpriseName").clear()
        driver.find_element_by_name("enterpriseName").send_keys(u"龙门水族摄影馆")
        driver.find_element_by_name("creditCode").clear()
        driver.find_element_by_name("creditCode").send_keys("130012992356")
        driver.find_element_by_id("startDate").click()
        driver.find_element_by_id("startDate").send_keys("2014-02-23")
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_name("regBankroll").clear()
        driver.find_element_by_name("regBankroll").send_keys("30000000")
        ##切换iframe
        driver.find_element_by_name("approvalDate").click()
        driver.find_element_by_name("approvalDate").send_keys("2015-10-23")
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))

        Select(driver.find_element_by_name("industryBaseCodeId")).select_by_value("8524")
        driver.find_element_by_name("busiScope").clear()
        driver.find_element_by_name("busiScope").send_keys(u"影像")
        driver.find_element_by_name("busiAddress").clear()
        driver.find_element_by_name("busiAddress").send_keys(u"榆林市")
        driver.find_element_by_name("idenCard").clear()
        driver.find_element_by_name("idenCard").send_keys("623455197801235624")
        Select(driver.find_element_by_name("nationalityBaseCodeId")).select_by_visible_text(u"中国")
        driver.find_element_by_name("emplNum").clear()
        driver.find_element_by_name("emplNum").send_keys("20")
        driver.find_element_by_name("investTotal").clear()
        driver.find_element_by_name("investTotal").send_keys("30000000")
        driver.find_element_by_name("domicile").clear()
        driver.find_element_by_name("domicile").send_keys(u"榆林市")
        driver.find_element_by_name("actualInvestDollar").clear()
        driver.find_element_by_name("actualInvestDollar").send_keys("5000000")
        driver.find_element_by_name("outSubcribeRMB").clear()
        driver.find_element_by_name("outSubcribeRMB").send_keys("200000")
        driver.find_element_by_id("regNum").clear()
        driver.find_element_by_id("regNum").send_keys("110213")
        driver.find_element_by_name("legalPerson").clear()
        driver.find_element_by_name("legalPerson").send_keys(u"宋毅")
        Select(driver.find_element_by_id("regOrgId")).select_by_visible_text(u"榆林市工商行政管理局")
        Select(driver.find_element_by_name("enterTypeBaseCodeId")).select_by_visible_text(u"个体")
        driver.find_element_by_name("regBankrollDollar").clear()
        driver.find_element_by_name("regBankrollDollar").send_keys("5000000")
        driver.find_element_by_name("fileNum").clear()
        driver.find_element_by_name("fileNum").send_keys("23")
        Select(driver.find_element_by_name("industryTypeBaseCodeId")).select_by_visible_text(u"文化、体育和娱乐业")
        #切换iframe
        driver.find_element_by_name("busiStopDate").click()
        driver.find_element_by_name("busiStopDate").send_keys("2020-10-23")
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_name("phone").clear()
        driver.find_element_by_name("phone").send_keys("029-45698523")
        driver.find_element_by_name("revokeDate").click()
        driver.find_element_by_name("revokeDate").send_keys("2020-10-22")
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_name("enterpriseTypeBaseCodeId")).select_by_value("1501140209620290")
        driver.find_element_by_name("investNum").clear()
        driver.find_element_by_name("investNum").send_keys("2")
        driver.find_element_by_name("investTotalDollar").clear()
        driver.find_element_by_name("investTotalDollar").send_keys("30000")
        driver.find_element_by_name("actualInvest").clear()
        driver.find_element_by_name("actualInvest").send_keys("30000")
        driver.find_element_by_name("outSubcribeDollar").clear()
        driver.find_element_by_name("outSubcribeDollar").send_keys("20000")
        driver.find_element_by_name("outPaidDollar").clear()
        driver.find_element_by_name("outPaidDollar").send_keys("20000")
        driver.find_element_by_css_selector("button.save-btn").click()
        Select(driver.find_element_by_id("depId")).select_by_visible_text(u"榆林市工商行政管理局榆阳分局")
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_id("enterpriseName").clear()
        driver.find_element_by_id("enterpriseName").send_keys(u"龙门水族摄影馆")
        driver.find_element_by_id("regNum").clear()
        driver.find_element_by_id("regNum").send_keys("110213")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"退出").click()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("111111")
    
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
