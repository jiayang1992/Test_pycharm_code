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
        driver.find_element_by_id("menu-sm6").click()
        driver.find_element_by_id("second-61").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=0 | ]]
        driver.find_element_by_id("villageId").click()
        driver.find_element_by_id("villageId").click()
        driver.find_element_by_name("projectType").click()
        Select(driver.find_element_by_name("projectType")).select_by_visible_text(u"教育（补助）培训")
        driver.find_element_by_css_selector("option[value=\"10\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectType").click()
        Select(driver.find_element_by_name("projectType")).select_by_visible_text(u"易地扶贫搬迁")
        driver.find_element_by_css_selector("option[value=\"20\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectType").click()
        Select(driver.find_element_by_name("projectType")).select_by_visible_text(u"金融扶贫")
        driver.find_element_by_css_selector("option[value=\"30\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_xpath("//form[@id='projectPayFormId']/div/ul/li[4]").click()
        driver.find_element_by_name("projectType").click()
        Select(driver.find_element_by_name("projectType")).select_by_visible_text(u"产业扶贫")
        driver.find_element_by_css_selector("option[value=\"40\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectType").click()
        Select(driver.find_element_by_name("projectType")).select_by_visible_text(u"整村推进")
        driver.find_element_by_css_selector("option[value=\"50\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectType").click()
        Select(driver.find_element_by_name("projectType")).select_by_visible_text(u"基础设施")
        driver.find_element_by_css_selector("option[value=\"70\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"产业项目")
        driver.find_element_by_css_selector("option[value=\"401\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"高校学历教育补助")
        driver.find_element_by_css_selector("option[value=\"101\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"职业高等学历教育补助")
        driver.find_element_by_css_selector("option[value=\"102\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"职业中等学历教育补助")
        driver.find_element_by_css_selector("option[value=\"103\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"劳动力短期技能培训")
        driver.find_element_by_css_selector("option[value=\"104\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"农民实用技术培训")
        driver.find_element_by_css_selector("option[value=\"105\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"雨露计划")
        driver.find_element_by_css_selector("option[value=\"106\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"致富带头人创业培训")
        driver.find_element_by_css_selector("option[value=\"107\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_xpath("//form[@id='projectPayFormId']/div/ul/li[5]").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"实用技术培训")
        driver.find_element_by_css_selector("option[value=\"108\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"集中安置")
        driver.find_element_by_css_selector("option[value=\"201\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"分散安置")
        driver.find_element_by_css_selector("option[value=\"202\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"(扶贫)小额信贷贴息")
        driver.find_element_by_css_selector("option[value=\"301\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"扶贫龙头企业贴息")
        driver.find_element_by_css_selector("option[value=\"302\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"其他")
        driver.find_element_by_css_selector("option[value=\"303\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"合作社")
        driver.find_element_by_css_selector("option[value=\"304\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"农业保险(产业保险)")
        driver.find_element_by_css_selector("option[value=\"305\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"人身保险(提供本省资金管理办法)")
        driver.find_element_by_css_selector("option[value=\"306\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"产业项目")
        driver.find_element_by_css_selector("option[value=\"401\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"资产收益扶贫")
        driver.find_element_by_css_selector("option[value=\"402\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectSType").click()
        Select(driver.find_element_by_name("projectSType")).select_by_visible_text(u"整村推进项目")
        driver.find_element_by_css_selector("option[value=\"501\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目新建")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"10\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目申请")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"20\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目审核并实施")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"30\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目验收")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"40\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目完成")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"50\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目检查")
        driver.find_element_by_css_selector("option[value=\"60\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("projectState").click()
        Select(driver.find_element_by_name("projectState")).select_by_visible_text(u"项目支付")
        driver.find_element_by_css_selector("select[name=\"projectState\"] > option[value=\"70\"]").click()
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"刘")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"王")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_name("userName").click()
        driver.find_element_by_name("userName").clear()
        driver.find_element_by_name("userName").send_keys(u"张")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("startDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/a").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | relative=parent | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame | index=1 | ]]
        driver.find_element_by_id("endDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[2]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("5700000005835996").click()
        # driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_projectId"))
        driver.find_element_by_id("closeId").click()
        time.sleep(5)
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
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
