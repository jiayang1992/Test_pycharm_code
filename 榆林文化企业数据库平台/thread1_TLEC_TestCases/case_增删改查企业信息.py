# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class VerifyAddAndDelete(unittest.TestCase):
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
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.maximize_window()
        driver.find_element_by_css_selector("li.unnum0").click()
        time.sleep(5)
        driver.find_element_by_id("menu-sm0").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("enterpriseName").clear()
        driver.find_element_by_id("enterpriseName").send_keys(u"延长石油")
        driver.find_element_by_id("regNum").clear()
        driver.find_element_by_id("regNum").send_keys("12")
        Select(driver.find_element_by_id("regOrgId")).select_by_visible_text(u"榆林市工商行政管理局")
        Select(driver.find_element_by_id("county")).select_by_visible_text(u"绥德县工商行政管理局")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        Select(driver.find_element_by_id("regOrgId")).select_by_visible_text(u"榆林市工商行政管理局")
        Select(driver.find_element_by_id("county")).select_by_visible_text(u"榆林市工商行政管理局榆阳分局")
        Select(driver.find_element_by_id("place")).select_by_visible_text(u"鼓楼工商所")
        Select(driver.find_element_by_id("enterTypeBaseCodeId")).select_by_visible_text(u"个体")
        #选择时间把只读数据改为可以写入的数据
        driver.find_element_by_id("queryBtn").click()
        js = "$('input[id=regDate]').attr('readonly',false),$('input[id=approvalDate]').attr('readonly',false)"
        driver.execute_script(js)
        driver.find_element_by_id("regDate").click()
        driver.find_element_by_id("regDate").send_keys('2013-11-20')
        driver.find_element_by_id("approvalDate").click()
        driver.find_element_by_id("approvalDate").send_keys('2014-11-21')
        #点击查询按钮
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("add").click()
        driver.find_element_by_name("enterpriseName").clear()
        driver.find_element_by_name("enterpriseName").send_keys(u"榆林市青岛啤酒产业基地")
        driver.find_element_by_name("creditCode").clear()
        driver.find_element_by_name("creditCode").send_keys("112")
        driver.find_element_by_id("startDate").click()
        driver.find_element_by_id("startDate").send_keys("2015-04-02")
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_name("regBankroll").clear()
        driver.find_element_by_name("regBankroll").send_keys("20000000")
        driver.find_element_by_name("approvalDate").click()
        driver.find_element_by_name("approvalDate").click()

        driver.find_element_by_name("approvalDate").send_keys("2015-06-14")
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_name("industryBaseCodeId")).select_by_value("2438")
        Select(driver.find_element_by_id("regOrgId")).select_by_visible_text(u"榆林市工商行政管理局")
        Select(driver.find_element_by_name("enterTypeBaseCodeId")).select_by_visible_text(u"个体")
        Select(driver.find_element_by_name("enterpriseTypeBaseCodeId")).select_by_visible_text(u"个体工商户")
        driver.find_element_by_css_selector("button.save-btn").click()
        Select(driver.find_element_by_id("depId")).select_by_visible_text(u"榆林市工商行政管理局榆阳分局")
        driver.find_element_by_id("regNum").clear()
        driver.find_element_by_id("regNum").send_keys("610123564879")
        driver.find_element_by_name("legalPerson").clear()
        driver.find_element_by_name("legalPerson").send_keys(u"闵长泽")
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_name("ids").click()
        driver.find_element_by_link_text(u"查看").click()
        driver.find_element_by_id("closeId").click()
        js = "$('input[id=regDate]').attr('readonly',false),$('input[id=approvalDate]').attr('readonly',false)"
        driver.execute_script(js)
        time.sleep(2)
        driver.find_element_by_id("regDate").click()
        driver.find_element_by_id("regDate").send_keys("2014-05-02")
        driver.find_element_by_id("approvalDate").click()
        driver.find_element_by_id("approvalDate").send_keys("2015-05-12")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("ids").click()
        driver.find_element_by_id("deleteAll").click()
        self.assertEqual(u"你确定要删除选中的1条记录吗？", self.close_alert_and_get_its_text())
        time.sleep(3)
        self.assertEqual(u"删除成功", self.close_alert_and_get_its_text())
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
