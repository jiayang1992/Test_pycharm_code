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
        driver.find_element_by_css_selector("li.unnum2").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.find_element_by_id("second-00").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"冬季考勤管理")
        #考勤开始
        driver.find_element_by_id("starTime").click()
        time.sleep(5)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("//html/body/div[1]/iframe"))
        driver.find_element_by_class_name("tB").click()
        driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/table/tbody/tr[2]/td[4]").click()
        driver.find_element_by_class_name("tE").click()
        driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/table/tbody/tr[1]/td[1]").click()
        driver.find_element_by_xpath("/html/body/div/div[4]/table/tbody/tr[1]/td[1]/input[5]").click()
        driver.find_element_by_xpath("/html/body/div/div[4]/div[3]/table/tbody/tr/td[1]").click()
        driver.find_element_by_id("dpOkInput").click()
        #考勤结束
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("endTime").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("//html/body/div[1]/iframe"))
        driver.find_element_by_class_name("tB").click()
        driver.find_element_by_xpath("/html/body/div/div[4]/div[1]/table/tbody/tr[4]/td[1]").click()
        driver.find_element_by_class_name("tE").click()
        driver.find_element_by_xpath("/html/body/div/div[4]/div[2]/table/tbody/tr[1]/td[1]").click()
        driver.find_element_by_xpath("/html/body/div/div[4]/table/tbody/tr[1]/td[1]/input[5]").click()
        driver.find_element_by_xpath("/html/body/div/div[4]/div[3]/table/tbody/tr/td[1]").click()
        driver.find_element_by_id("dpOkInput").click()
        #配置开始
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("startDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("startDate").click()
       #清除选择时间快速选择
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[6]").click()
        driver.find_element_by_id("dpClearInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("startDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpQS").click()
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("startDate").click()
       #今天
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpTodayInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        #配置结束
        driver.find_element_by_id("endDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[2]").click()
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_class_name("save-btn").click()
        #修改
        driver.find_element_by_link_text(u"修改").click()
        driver.find_element_by_id("startDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.find_element_by_id("dpOkInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_class_name("save-btn").click()
        #返回修改
        driver.find_element_by_link_text(u"修改").click()
        driver.find_element_by_class_name("back-btn").click()
        #查询
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"冬季考勤")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys("2018")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("resetBtn").click()

        #全选删除功能
        driver.find_element_by_id("firstCheckbox").click()
        self.accept_next_alert = False
        driver.find_element_by_id("toDelBtn").click()
        self.assertEqual(u"你确定要删除选中的1条记录吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_id("toDelBtn").click()
        self.assertEqual(u"你确定要删除选中的1条记录吗？", self.close_alert_and_get_its_text())
        time.sleep(5)
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
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
