# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        option = webdriver.ChromeOptions()
        executable_path = "C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
        os.environ['webdriver.chrome.driver'] = executable_path
        self.driver = webdriver.Chrome(executable_path, chrome_options=option)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://124.115.106.140:7001/manage/user/home")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").click()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").click()
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("1")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum4").click()
        driver.find_element_by_id("menu-sm2").click()
        driver.find_element_by_id("second-20").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        #点击新增按钮，在新增页面点击返回安钮
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_id("catalogSelect").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"测试")
        driver.find_element_by_id("status").click()
        driver.find_element_by_id("remark").click()
        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys(u"无")
        driver.find_element_by_id("saveRoleBtn").click()
        print("成功从新增页面返回")
        #点击新增按钮，在新增页面点击新增，测试新增返回功能
        driver.find_element_by_id("toAddBtn").click()
        driver.find_element_by_id("catalogSelect").click()
        driver.find_element_by_id("catalogSelect").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"测试")
        driver.find_element_by_id("remark").click()
        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys(u"无")
        driver.find_element_by_css_selector("button.save-btn").click()
        print("新增部门成功")
        #输入部门名称，点击查询按钮，测试查询功能
        driver.find_element_by_id("dname").click()
        driver.find_element_by_id("dname").clear()
        driver.find_element_by_id("dname").send_keys(u"测试")
        driver.find_element_by_id("queryBtn").click()
        #测试编辑按钮
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("remark").click()
        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys(u"测试")
        driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_id("dname").click()
        driver.find_element_by_id("dname").clear()
        driver.find_element_by_id("dname").send_keys(u"测试")
        driver.find_element_by_id("queryBtn").click()
        #测试成员管理页面的新增功能
        driver.find_element_by_link_text(u"成员管理").click()
        driver.find_element_by_css_selector("input.save-btn").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"李红")
        driver.find_element_by_id("sex").click()
        Select(driver.find_element_by_id("sex")).select_by_visible_text(u"女")
        driver.find_element_by_css_selector("option[value=\"1\"]").click()
        driver.find_element_by_id("idCard").click()
        driver.find_element_by_id("idCard").clear()
        driver.find_element_by_id("idCard").send_keys("627032198902031542")
        driver.find_element_by_id("telePhone").click()
        driver.find_element_by_id("telePhone").clear()
        driver.find_element_by_id("telePhone").send_keys("13286592314")
        driver.find_element_by_id("dutyTitle").click()
        driver.find_element_by_id("dutyTitle").clear()
        driver.find_element_by_id("dutyTitle").send_keys(u"无")
        driver.find_element_by_id("nativePlace").click()
        driver.find_element_by_id("nativePlace").clear()
        driver.find_element_by_id("nativePlace").send_keys(u"中国")
        driver.find_element_by_id("address").click()
        driver.find_element_by_id("address").clear()
        driver.find_element_by_id("address").send_keys(u"榆林")
        driver.find_element_by_id("email").click()
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("56243819@qq.com")
        driver.find_element_by_id("remark").click()
        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys(u"无")
        driver.find_element_by_css_selector("button.save-btn").click()
        print("在成员管理页面，成功新增人员")
        #测试成员管理页面的提取至平台功能
        driver.find_element_by_xpath("//form[@id='mainForm']/div[2]/table/tbody/tr[2]/td").click()
        driver.find_element_by_name("ids").click()
        driver.find_element_by_name("ids").click()
        driver.find_element_by_css_selector("li.formli > input.save-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectDepartId"))
        driver.find_element_by_id("treeDemo_1_span").click()
        driver.find_element_by_id("treeDemo_1_check").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        self.assertEqual(u"已成功提取至平台层!", self.close_alert_and_get_its_text())
        print("人员成功提取至平台层")
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        #测试成员管理页面的人员合并功能
        driver.find_element_by_id("optButton").click()
        driver.find_element_by_name("newDep").click()
        driver.find_element_by_link_text(u"确认合并").click()
        self.assertEqual(u"待合并的人员信息不能为空!", self.close_alert_and_get_its_text())
        driver.find_element_by_name("newDep").click()
        driver.find_element_by_css_selector("div.sm-dialog-close").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_css_selector("button.back-btn").click()
        driver.find_element_by_link_text(u"返回上级").click()
        #测试成员管理页面的查询、重置、导出本页功能
        driver.find_element_by_link_text(u"成员管理").click()
        driver.find_element_by_id("name").click()
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"李红")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("telephone").click()
        driver.find_element_by_id("telephone").clear()
        driver.find_element_by_id("telephone").send_keys("132")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_xpath(u"//button[@value='导出本页']").click()
        driver.find_element_by_link_text(u"返回上级").click()
        #测试驻村部门管理页面的部门合并功能
        driver.find_element_by_id("dname").click()
        driver.find_element_by_id("dname").clear()
        driver.find_element_by_id("dname").send_keys(u"测试")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_xpath("//table[@id='treegrid']/tbody/tr[2]/td").click()
        driver.find_element_by_id("ids").click()
        driver.find_element_by_id("ids").click()
        driver.find_element_by_xpath("(//input[@id='ids'])[2]").click()
        driver.find_element_by_id("optButton").click()
        driver.find_element_by_name("newDep").click()
        driver.find_element_by_xpath("(//input[@name='newDep'])[2]").click()
        driver.find_element_by_link_text(u"确认合并").click()
        time.sleep(3)
        self.assertEqual(u"合并部门成功!", self.close_alert_and_get_its_text())
        print("部门合并成功")
        driver.find_element_by_link_text(u"成员管理").click()
        driver.find_element_by_link_text(u"返回上级").click()
        #测试没有删除该部门下的人员信息，能否删除部门
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除当前部门吗[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除当前部门吗[\s\S]$")
        self.assertEqual(u"删除失败，该先删除该部门下的人员信息！", self.close_alert_and_get_its_text())
        time.sleep(3)
        #合并管理页面下的人员信息
        driver.find_element_by_link_text(u"成员管理").click()
        driver.find_element_by_id("firstCheckbox").click()
        # driver.find_element_by_name("ids").click()
        # driver.find_element_by_name("ids").click()
        # driver.find_element_by_xpath("(//input[@name='ids'])[2]").click()
        driver.find_element_by_id("optButton").click()
        # driver.find_element_by_name("newDep").click()
        driver.find_element_by_xpath("//div[@id='showOprate']/table/tbody/tr[3]/td[5]").click()
        driver.find_element_by_xpath("(//input[@name='newDep'])[2]").click()
        driver.find_element_by_link_text(u"确认合并").click()
        time.sleep(3)
        self.assertEqual(u"合并人员信息成功!", self.close_alert_and_get_its_text())
        print("人员合并成功")
        #删除成员管理页面下的人员信息
        driver.find_element_by_id("firstCheckbox").click()
        self.accept_next_alert = False
        driver.find_element_by_class_name("default-btn").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定要删除选中的人员吗?[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_class_name("default-btn").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定要删除选中的人员吗?[\s\S]$")
        print("成功删除人员信息")
        driver.find_element_by_link_text(u"返回上级").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        #删除驻村部门管理下的部门
        driver.find_element_by_id("dname").click()
        driver.find_element_by_id("dname").clear()
        driver.find_element_by_id("dname").send_keys(u"测试")
        driver.find_element_by_id("queryBtn").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除当前部门吗[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除当前部门吗[\s\S]$")
        print("成功删除部门")
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
