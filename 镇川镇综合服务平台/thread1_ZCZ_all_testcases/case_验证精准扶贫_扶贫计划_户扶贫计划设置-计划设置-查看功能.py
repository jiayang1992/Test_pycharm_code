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
        driver.find_element_by_id("menu-sm4").click()
        driver.find_element_by_id("second-44").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_name("town").click()
        driver.find_element_by_name("town").click()
        driver.find_element_by_id("villageId").click()
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        driver.find_element_by_css_selector("option[value=\"610802028001\"]").click()
        driver.find_element_by_id("teamId").click()
        driver.find_element_by_name("leadResult").click()
        driver.find_element_by_name("leadResult").click()
        driver.find_element_by_name("poorAttri").click()
        driver.find_element_by_name("poorAttri").click()
        driver.find_element_by_name("identify").click()
        driver.find_element_by_name("identify").click()
        driver.find_element_by_name("tpAttri").click()
        Select(driver.find_element_by_name("tpAttri")).select_by_visible_text(u"未脱贫")
        driver.find_element_by_css_selector("option[value=\"0\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"张")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("cardNo").click()
        driver.find_element_by_name("cardNo").clear()
        driver.find_element_by_name("cardNo").send_keys("610")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("cardNo").click()
        driver.find_element_by_name("cardNo").clear()
        driver.find_element_by_name("cardNo").send_keys("6127211989")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("cardNo").click()
        driver.find_element_by_name("cardNo").clear()
        driver.find_element_by_name("cardNo").send_keys("6127211932")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("3117031598").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_id("switch-big5").click()
        driver.find_element_by_id("switch-big6").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("closeId").click()
        time.sleep(5)
        driver.find_element_by_link_text(u"计划设置").click()
        driver.find_element_by_id("taskName0").click()
        driver.find_element_by_id("taskName0").clear()
        driver.find_element_by_id("taskName0").send_keys(u"救助留守儿童")
        driver.find_element_by_id("planBeginDate00").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[4]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("planEndDate00").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[5]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("taskDesc0").click()
        driver.find_element_by_id("methodPercent1").click()
        driver.find_element_by_id("methodPercent1").clear()
        driver.find_element_by_id("methodPercent1").send_keys("40")
        driver.find_element_by_id("methodPercent1").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=methodPercent1 | ]]
        driver.find_element_by_id("taskDesc0").clear()
        driver.find_element_by_id("taskDesc0").send_keys(u"呵呵")
        driver.find_element_by_id("methodPercent0").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=methodPercent0 | ]]
        driver.find_element_by_id("methodPercent0").clear()
        driver.find_element_by_id("methodPercent0").send_keys("30")
        driver.find_element_by_id("methodPercent0").click()
        driver.find_element_by_id("methodPercent1").clear()
        driver.find_element_by_id("methodPercent1").send_keys("20")
        driver.find_element_by_css_selector("#firstLine0 > button.save-btn").click()
        driver.find_element_by_css_selector("#firstLine0 > #saveBtn").click()
        driver.find_element_by_link_text(u"移除").click()
        driver.find_element_by_css_selector("#firstLine0 > #saveBtn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_id("methodPercent1").click()
        driver.find_element_by_id("methodPercent1").clear()
        driver.find_element_by_id("methodPercent1").send_keys("20")
        driver.find_element_by_css_selector("#childTalbe10 > tbody > tr > td.td-right > #taskName0").click()
        driver.find_element_by_css_selector("#childTalbe10 > tbody > tr > td.td-right > #taskName0").clear()
        driver.find_element_by_css_selector("#childTalbe10 > tbody > tr > td.td-right > #taskName0").send_keys("1")
        driver.find_element_by_css_selector("#childTalbe10 > tbody > tr > td.td-right > img").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        # driver.find_element_by_id("planBeginDate10").click()
        # driver.switch_to_default_content()
        # driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        # driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[4]/img[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_xpath("//*[@id='planBeginDate10']").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[4]/td[3]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("taskDesc1").click()
        driver.find_element_by_id("taskDesc1").clear()
        driver.find_element_by_id("taskDesc1").send_keys(u"呵呵")
        driver.find_element_by_id("taskDesc1").click()
        driver.find_element_by_css_selector("#firstLine1 > #saveBtn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_id("methodPercent4").clear()
        driver.find_element_by_id("methodPercent4").send_keys("60")
        driver.find_element_by_css_selector("#childTalbe4 > tbody > tr > td.td-right > input[name=\"taskNameArray\"]").click()
        driver.find_element_by_css_selector("#childTalbe4 > tbody > tr > td.td-right > input[name=\"taskNameArray\"]").clear()
        driver.find_element_by_css_selector("#childTalbe4 > tbody > tr > td.td-right > input[name=\"taskNameArray\"]").send_keys("5")
        driver.find_element_by_id("planBeginDate4").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("planEndDate4").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[5]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[3]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("taskDesc4").click()
        driver.find_element_by_id("taskDesc4").clear()
        driver.find_element_by_id("taskDesc4").send_keys(u"给他")
        driver.find_element_by_css_selector("#firstLine4 > #saveBtn").click()
        self.assertEqual(u"计划权重设置超出100%,请调整每步计划在整个计划中的所占权重!", self.close_alert_and_get_its_text())
        driver.find_element_by_id("methodPercent4").click()
        driver.find_element_by_id("methodPercent4").clear()
        driver.find_element_by_id("methodPercent4").send_keys("10")
        driver.find_element_by_css_selector("#firstLine4 > #saveBtn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("#firstLine4 > #saveBtn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("button.back-btn").click()
        driver.find_element_by_link_text(u"计划设置").click()
        self.accept_next_alert = False
        driver.find_element_by_css_selector("#mainForm4 > #detailsSetting > tbody > tr.saveVal > td.td-left > #saveBtn").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^清空计划执行流程：1\.删除此步计划下各个任务相关的日志\(扶贫动态\)；2\.删除此步计划的所有任务；3\.清空此步计划；计划清空后不可恢复,确认要将此步计划清空吗[\s\S]$")
        self.accept_next_alert = True
        driver.find_element_by_css_selector("#mainForm4 > #detailsSetting > tbody > tr.saveVal > td.td-left > #saveBtn").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^清空计划执行流程：1\.删除此步计划下各个任务相关的日志\(扶贫动态\)；2\.删除此步计划的所有任务；3\.清空此步计划；计划清空后不可恢复,确认要将此步计划清空吗[\s\S]$")
        self.assertEqual(u"此步计划已清空!", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("button.back-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
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
