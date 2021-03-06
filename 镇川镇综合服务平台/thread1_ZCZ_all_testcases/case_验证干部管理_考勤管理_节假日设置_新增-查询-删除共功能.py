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
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum2").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.find_element_by_id("second-02").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        #新增
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_css_selector("img").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[3]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_name("dayType")).select_by_visible_text("国家节假日")
        driver.find_element_by_css_selector("input.save-btn").click()
        print("新增成功")
        #从新增页面返回
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_css_selector("button.back-btn").click()
        #再次新增
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_css_selector("img").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_name("dayType")).select_by_visible_text(u"国家节假日")
        driver.find_element_by_css_selector("input.save-btn").click()
        #修改
        driver.find_element_by_link_text(u"修改").click()
        driver.find_element_by_css_selector("img").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpTodayInput").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("img").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpClearInput").click()
        print("成功修改")
        #快速选择
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("img").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_id("dpQS").click()
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[2]/td").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_name("dayType")).select_by_visible_text(u"特殊工作日")
        driver.find_element_by_css_selector("input.save-btn").click()
        #查询
        driver.find_element_by_name("startTime").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_name("endTime").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_class_name("form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以时间段查询，在这个时间段查询到的结果有%d条"%int(value))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("dayType").click()
        Select(driver.find_element_by_name("dayType")).select_by_visible_text("国家节假日")
        value1 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以类型进行查询，搜索到的结果有%d条" % int(value1))
        driver.find_element_by_id("resetBtn").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"你确定要删除这条记录吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"你确定要删除这条记录吗？", self.close_alert_and_get_its_text())
        time.sleep(3)
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        print("成功删除")
        value2 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("点击删除一条信息后还有%d条" % int(value2))
        driver.find_element_by_id("firstCheckbox").click()
        self.accept_next_alert = False
        driver.find_element_by_id("toDelBtn").click()
        self.assertEqual(u"你确定要删除选中的1条记录吗？",self.close_alert_and_get_its_text())
        driver.find_element_by_id("toDelBtn").click()
        self.assertEqual(u"你确定要删除选中的1条记录吗？", self.close_alert_and_get_its_text())
        time.sleep(3)
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        value3 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("点击全部删除后还有%d条信息" % int(value3))
        print("此条case运行成功")
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
