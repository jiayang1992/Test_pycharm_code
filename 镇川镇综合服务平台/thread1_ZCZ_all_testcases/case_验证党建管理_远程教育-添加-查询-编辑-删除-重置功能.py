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
        driver.find_element_by_id("menu-sm7").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_1_span").click()
        driver.find_element_by_id("partGroupTree_1_switch").click()
        driver.find_element_by_id("partGroupTree_3_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_css_selector("input.form-btn").click()
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"测试")
        driver.find_element_by_id("address").clear()
        driver.find_element_by_id("address").send_keys(u"绥德")
        driver.find_element_by_id("programme").clear()
        driver.find_element_by_id("programme").send_keys(u"李三")
        driver.find_element_by_id("meetingDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_name("actualNumber").clear()
        driver.find_element_by_name("actualNumber").send_keys("36")
        driver.find_element_by_name("meetingTime").clear()
        driver.find_element_by_name("meetingTime").send_keys("120")
        driver.find_element_by_name("recordName").clear()
        driver.find_element_by_name("recordName").send_keys(u"张珂")
        driver.find_element_by_name("content").clear()
        driver.find_element_by_name("content").send_keys(u"无")
        driver.find_element_by_class_name("swfupload").click()
        os.system("uploadpicture.exe")
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"你确定删除此附件吗？", self.close_alert_and_get_its_text())
        Select(driver.find_element_by_name("fileFlags")).select_by_visible_text(u"参会人员合影")
        driver.find_element_by_link_text(u"删除").click()
        self.assertEqual(u"你确定删除此附件吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("button.dialog-btn").click()
        driver.find_element_by_css_selector("input.form-btn").click()
        driver.find_element_by_id("closeId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_3_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        value2 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("该党支部共有%d条结果" % int(value2))
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"测试")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("搜索会议标题为'测试'的共有%d条结果"%int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        value1 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("重置标题搜索后有%d条结果" % int(value1))
        if value1 != value2:
            print("重置失败")
        else:
            print("成功重置")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_3_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_id("startDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        starttime1 = driver.find_element_by_id("startDate").get_attribute("value")
        driver.find_element_by_id("endDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[4]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        endtime1 = driver.find_element_by_id("endDate").get_attribute("value")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        print("开始时间%s" % str(starttime1), "结束时间%s" % str(endtime1))
        driver.find_element_by_css_selector("button.form-btn").click()
        value3 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("按时间范围查询到%d条结果" % int(value3))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        value4 = driver.find_element_by_id("totalNum").get_attribute("value")
        print("重置时间范围后有%d条结果" % int(value4))
        if value4 != value2:
            print("重置失败")
        else:
            print("成功重置")
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_3_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"测试")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_link_text(u"查看").click()
        # driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewthreepartyId"))
        driver.find_element_by_id("closeId").click()
        time.sleep(5)
        driver.find_element_by_link_text(u"编辑").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updthreepartyId"))
        # Select(driver.find_element_by_name("fileFlags")).select_by_visible_text(u"参会人员合影")
        driver.find_element_by_css_selector("button.dialog-btn.date-sava-Vaild").click()
        self.assertEqual(u"修改成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"测试")
        driver.find_element_by_css_selector("button.form-btn").click()
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此会议信息吗[\s\S]$")
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此会议信息吗[\s\S]$")
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_3_span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        time.sleep(5)
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"测试")
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
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
