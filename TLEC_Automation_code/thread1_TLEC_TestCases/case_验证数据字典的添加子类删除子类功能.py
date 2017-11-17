# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class Add_subclasses(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path,chrome_options=options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://101.201.41.228:6800/manage/user/home"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        #登录
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        #进入系统管理
        driver.find_element_by_css_selector("li.unnum2").click()
        #进入模块管理
        driver.find_element_by_id("menu-sm1").click()
        #进入数据字典
        driver.find_element_by_id("second-11").click()
        #切换框架到iframeClass
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        #清除大类名称
        driver.find_element_by_id("codename").clear()
        driver.find_element_by_id("codename").send_keys(u"测试")
        #点击查询按钮
        driver.find_element_by_id("queryData").click()
        #点击重置按钮
        driver.find_element_by_id("resetBtn").click()
        #点击添加按钮
        driver.find_element_by_css_selector("button.edit-btn").click()
        #清除大类名称并重新输入
        driver.find_element_by_id("codename").clear()
        driver.find_element_by_id("codename").send_keys(u"测试01")
        #点击保存按钮
        driver.find_element_by_css_selector("button.save-btn").click()
        #点击编辑按钮
        driver.find_element_by_link_text(u"编辑").click()
        #清除大类名称并重新输入
        driver.find_element_by_id("codename").clear()
        driver.find_element_by_id("codename").send_keys(u"测试001")
        #点击保存按钮
        driver.find_element_by_css_selector("button.save-btn").click()
        #点击管理子类
        driver.find_element_by_link_text(u"管理子类").click()
        #点击添加按钮
        driver.find_element_by_css_selector("button.edit-btn").click()
        #清除编码名称并重新输入
        driver.find_element_by_id("codename").clear()
        driver.find_element_by_id("codename").send_keys(u"测试001")
        #清除注解码并重新输入
        driver.find_element_by_id("codeEnCode").clear()
        driver.find_element_by_id("codeEnCode").send_keys("1101")
        #编辑备注
        driver.find_element_by_name("mark").clear()
        driver.find_element_by_name("mark").send_keys(u"无")
        #点击保存按钮
        driver.find_element_by_css_selector("button.save-btn").click()
        #点击添加子类
        driver.find_element_by_link_text(u"添加子类").click()
        #点击添加按钮
        driver.find_element_by_css_selector("button.edit-btn").click()
        #清除子类名称并重新输入
        driver.find_element_by_id("codename").clear()
        driver.find_element_by_id("codename").send_keys(u"测试001")
        #点击保存按钮
        driver.find_element_by_css_selector("button.save-btn").click()
        
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("backBtn").click()
        driver.find_element_by_link_text(u"管理子类").click()
        driver.find_element_by_link_text(u"添加子类").click()
        driver.find_element_by_name("ids").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除选择的记录[\s\S]$")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除选择的记录[\s\S]$")
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        driver.find_element_by_name("ids").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("codename").clear()
        driver.find_element_by_id("codename").send_keys(u"测试0010")
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_name("ids").click()
        self.accept_next_alert = False
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除选择的记录[\s\S]$")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除选择的记录[\s\S]$")
        driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除该条记录吗[\s\S]$")
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
