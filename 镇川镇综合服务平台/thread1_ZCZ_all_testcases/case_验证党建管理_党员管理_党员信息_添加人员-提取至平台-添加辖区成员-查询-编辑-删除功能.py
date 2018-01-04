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
        driver.find_element_by_id("menu-sm2").click()
        driver.find_element_by_id("second-20").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectFrame |  | ]]
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_xpath(u"//input[@value='添 加 人 员']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyMemberId"))
        driver.find_element_by_id("switch-big1").click()
        driver.find_element_by_css_selector("button.dialog-btn").click()
        driver.find_element_by_id("memberNameId").clear()
        driver.find_element_by_id("memberNameId").send_keys(u"杨舒羽")
        Select(driver.find_element_by_id("sexId")).select_by_visible_text(u"女")
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("627018257634891425")
        driver.find_element_by_id("birthDay").click()
        driver.find_element_by_id("birthDay").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("612701199501251423")
        driver.find_element_by_xpath("//img[@onclick=\"WdatePicker({dateFmt:'yyyy-MM-dd',maxDate:'#F{$dp.$D(\\'joinPartyDate\\')}'})\"]").click()
        driver.find_element_by_xpath("//img[@onclick=\"WdatePicker({dateFmt:'yyyy-MM-dd',maxDate:'#F{$dp.$D(\\'joinPartyDate\\')}'})\"]").click()
        driver.find_element_by_id("birthDay").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyMemberId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("joinPartyDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[6]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[5]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyMemberId"))

        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        Select(driver.find_element_by_id("politicsStatusId")).select_by_visible_text(u"民进会员")
        driver.find_element_by_id("joinLeagueDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[6]/td[4]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addPartyMemberId"))

        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        Select(driver.find_element_by_id("memberType")).select_by_visible_text(u"正常党员")
        driver.find_element_by_id("nativePlaceId").clear()
        driver.find_element_by_id("nativePlaceId").send_keys(u"中国")
        driver.find_element_by_name("joinPartyGroup").clear()
        driver.find_element_by_name("joinPartyGroup").send_keys(u"陕西省榆林市")
        driver.find_element_by_name("personalIdentity").clear()
        driver.find_element_by_name("personalIdentity").send_keys(u"学生")
        Select(driver.find_element_by_id("educationId")).select_by_visible_text(u"大学专科")
        Select(driver.find_element_by_id("educationId")).select_by_visible_text(u"大学本科")
        driver.find_element_by_id("contactPhoneId").clear()
        driver.find_element_by_id("contactPhoneId").send_keys("15708125364")
        driver.find_element_by_id("addrFamilyId").clear()
        driver.find_element_by_id("addrFamilyId").send_keys(u"陕西榆林")
        driver.find_element_by_name("bakDes").clear()
        driver.find_element_by_name("bakDes").send_keys(u"无")
        driver.find_element_by_name("aLineOf").clear()
        driver.find_element_by_name("aLineOf").send_keys(u"无")
        driver.find_element_by_name("newClass").clear()
        driver.find_element_by_name("newClass").send_keys("2000")
        driver.find_element_by_name("workUnits").clear()
        driver.find_element_by_name("workUnits").send_keys(u"无")
        driver.find_element_by_id("professionalId").clear()
        driver.find_element_by_id("professionalId").send_keys(u"无")
        Select(driver.find_element_by_name("mediationType")).select_by_visible_text(u"集体所有制")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_link_text(u"编辑").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyMemberId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big1").click()
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_link_text(u"编辑").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyMemberId"))
        driver.find_element_by_id("switch-big1").click()
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_css_selector("td > button.dialog-btn").click()
        self.assertEqual(u"开始时间不能为空!", self.close_alert_and_get_its_text())
        driver.find_element_by_id("startDateId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[6]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyMemberId"))
        driver.find_element_by_id("endDateId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[1]").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyMemberId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("compNameId").clear()
        driver.find_element_by_id("compNameId").send_keys(u"上海建筑")
        driver.find_element_by_id("workPositionId").clear()
        driver.find_element_by_id("workPositionId").send_keys(u"工人")
        driver.find_element_by_css_selector("td > button.dialog-btn").click()
        self.assertEqual(u"新增成功！", self.close_alert_and_get_its_text())
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此工作履历吗[\s\S]$")
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此工作履历吗[\s\S]$")
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_link_text(u"编辑").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyMemberId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("startDateId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[3]/td[6]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyMemberId"))
        driver.find_element_by_id("endDateId").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[1]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updPartyMemberId"))
        driver.find_element_by_id("compNameId").clear()
        driver.find_element_by_id("compNameId").send_keys(u"云澜软件")
        driver.find_element_by_id("workPositionId").clear()
        driver.find_element_by_id("workPositionId").send_keys(u"测试")
        driver.find_element_by_css_selector("td > button.dialog-btn").click()
        self.assertEqual(u"新增成功！", self.close_alert_and_get_its_text())
        driver.find_element_by_css_selector("button.dialog-btn.date-sava-Vaild").click()
        self.assertEqual(u"修改成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_link_text(u"查看").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewPartyMemberId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_css_selector("li > #closeId").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_name("memberName").clear()
        driver.find_element_by_name("memberName").send_keys(u"杨舒羽")
        time.sleep(3)
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_id("startDate").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[1]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[2]/td[6]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("endDate").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[5]/a").click()
        driver.find_element_by_xpath("//*[@id='dpTitle']/div[2]/a").click()
        driver.find_element_by_xpath("/html/body/div/div[3]/table/tbody/tr[7]/td[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_css_selector("button.form-btn").click()
        driver.find_element_by_name("ids").click()
        driver.find_element_by_css_selector("input.form-btn").click()
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_name("ids").click()
        driver.find_element_by_css_selector("ul.form-ul > li.formli > input.form-btn").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectDepartId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("treeDemo_1_switch").click()
        driver.find_element_by_id("treeDemo_1_switch").click()
        time.sleep(3)
        driver.find_element_by_id("treeDemo_3_span").click()
        driver.find_element_by_id("treeDemo_3_switch").click()
        driver.find_element_by_id("treeDemo_4_check").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        self.assertEqual(u"已成功提取至平台层!", self.close_alert_and_get_its_text())
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_link_text(u"查看").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_viewPartyMemberId"))
        driver.find_element_by_id("closeId").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("partGroupTree_1_span").click()
        driver.find_element_by_id("partGroupTree_1_span").click()
        driver.find_element_by_id("partGroupTree_3_span").click()
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_xpath(u"//input[@value='添加辖区成员']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_selectCadreByArea"))
        driver.find_element_by_id("personName").clear()
        driver.find_element_by_id("personName").send_keys(u"张")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("telPhone").clear()
        driver.find_element_by_id("telPhone").send_keys("133")
        driver.find_element_by_id("queryBtn").click()
        # name = ['张','刘','王','孙','李']
        # for i in name:
        #     driver.find_element_by_id("personName").clear()
        #     driver.find_element_by_id("personName").send_keys(u"刘")
        #     driver.find_element_by_id("queryBtn").click()
        # tel = ['132','158','159','135','133']
        # for j in tel:
        #     driver.find_element_by_id("telPhone").clear()
        #     driver.find_element_by_id("telPhone").send_keys("159")
        #     driver.find_element_by_id("queryBtn").click()
        Select(driver.find_element_by_id("dutyLevel")).select_by_visible_text(u"科员级")
        driver.find_element_by_id("queryBtn").click()
        Select(driver.find_element_by_id("dutyLevel")).select_by_visible_text(u"乡科级正职")
        driver.find_element_by_id("queryBtn").click()
        Select(driver.find_element_by_id("dutyLevel")).select_by_visible_text(u"乡科级副职")
        driver.find_element_by_id("queryBtn").click()
        Select(driver.find_element_by_id("dutyLevel")).select_by_visible_text(u"办事员级")
        driver.find_element_by_id("queryBtn").click()
        Select(driver.find_element_by_id("dutyLevel")).select_by_visible_text(u"未定职")
        driver.find_element_by_id("queryBtn").click()
        Select(driver.find_element_by_id("dutyLevel")).select_by_visible_text(u"全部")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_name("ids").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("iframeMenuEdit"))
        driver.find_element_by_class_name(" aui_state_highlight").click()
        self.assertEqual(u"添加辖区成员成功!", self.close_alert_and_get_its_text())
        # driver.find_element_by_xpath(u"//input[@value='添加辖区成员']").click()
        # driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        # ERROR: Caught exception [Error: Dom locators are not implemented yet!]
        self.accept_next_alert = False
        driver.find_element_by_xpath(u"//*[@id='partyMemberFormId']/div[3]/table/tbody/tr[3]/td[15]/a[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此党员信息吗[\s\S]$")
        driver.find_element_by_xpath(u"//*[@id='partyMemberFormId']/div[3]/table/tbody/tr[3]/td[15]/a[3]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此党员信息吗[\s\S]$")
        self.assertEqual(u"删除成功！", self.close_alert_and_get_its_text())
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
