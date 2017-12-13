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
        driver.find_element_by_css_selector("li.unnum1").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath(u"//button[@value='新增']").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addFamilyId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=fbMainContainer | ]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_name("isInStu")).select_by_visible_text(u"是")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("15709277256")
        Select(driver.find_element_by_name("poorAttri")).select_by_visible_text(u"一般贫困户")
        driver.find_element_by_name("houseNum").clear()
        driver.find_element_by_name("houseNum").send_keys("5")
        driver.find_element_by_name("bankName").clear()
        driver.find_element_by_name("bankName").send_keys(u"农业银行")
        driver.find_element_by_name("bankNo").clear()
        driver.find_element_by_name("bankNo").send_keys("610123654871234568")
        driver.find_element_by_name("hlCardNo").clear()
        driver.find_element_by_name("hlCardNo").send_keys("11111111")
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("usernameId").clear()
        driver.find_element_by_id("usernameId").send_keys(u"张三")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之子")
        driver.find_element_by_id("cardnoId").clear()
        driver.find_element_by_id("cardnoId").send_keys("613158198910221452")
        Select(driver.find_element_by_id("politicsId")).select_by_visible_text(u"中共党员")
        Select(driver.find_element_by_id("edustatenameId")).select_by_visible_text(u"大专及以上")
        Select(driver.find_element_by_id("healthstatenameId")).select_by_visible_text(u"健康")
        Select(driver.find_element_by_id("workSkillId")).select_by_visible_text(u"普通劳动力")
        Select(driver.find_element_by_id("nationalnameId")).select_by_visible_text(u"汉族")
        Select(driver.find_element_by_id("stustatenameId")).select_by_visible_text(u"大专及以上")
        Select(driver.find_element_by_id("laborstatenameId")).select_by_visible_text(u"乡（镇）内务工")
        driver.find_element_by_id("laborTimeId").clear()
        driver.find_element_by_id("laborTimeId").send_keys("2400")
        Select(driver.find_element_by_id("lifeStateId")).select_by_visible_text(u"正常")
        driver.find_element_by_css_selector("td > button.dialog-btn").click()
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath(u"//button[@value='新增']").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addFamilyId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath(u"//button[@value='新增']").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addFamilyId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_id("switch-big1").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_name("tgArea").clear()
        driver.find_element_by_name("tgArea").send_keys("1200")
        driver.find_element_by_name("mcArea").clear()
        driver.find_element_by_name("mcArea").send_keys("120")
        driver.find_element_by_name("gjArea").clear()
        driver.find_element_by_name("gjArea").send_keys("120")
        driver.find_element_by_name("gdArea").clear()
        driver.find_element_by_name("gdArea").send_keys("100")
        driver.find_element_by_name("lgArea").clear()
        driver.find_element_by_name("lgArea").send_keys("120")
        driver.find_element_by_name("ldArea").clear()
        driver.find_element_by_name("ldArea").send_keys("120")
        driver.find_element_by_name("smArea").clear()
        driver.find_element_by_name("smArea").send_keys("100")
        driver.find_element_by_name("distance").clear()
        driver.find_element_by_name("distance").send_keys("1200")
        driver.find_element_by_name("houseArea").clear()
        driver.find_element_by_name("houseArea").send_keys("120")
        Select(driver.find_element_by_name("isWaterDiff")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("fuelType")).select_by_visible_text(u"柴草")
        Select(driver.find_element_by_name("roadType")).select_by_visible_text(u"泥土路")
        Select(driver.find_element_by_name("isWaterSafe")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("houseLevel")).select_by_visible_text(u"C级")
        Select(driver.find_element_by_name("isTv")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("isToilet")).select_by_visible_text(u"是")
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_name("salaryIncome").clear()
        driver.find_element_by_name("salaryIncome").send_keys("20")
        driver.find_element_by_name("estateIncome").clear()
        driver.find_element_by_name("estateIncome").send_keys("20")
        driver.find_element_by_name("fiveGold").clear()
        driver.find_element_by_name("fiveGold").send_keys("20")
        driver.find_element_by_name("yearIncome").clear()
        driver.find_element_by_name("yearIncome").send_keys("50000")
        driver.find_element_by_name("planGold").clear()
        driver.find_element_by_name("planGold").send_keys("120")
        driver.find_element_by_name("ecoGold").clear()
        driver.find_element_by_name("ecoGold").send_keys("230")
        driver.find_element_by_name("pureIncome").clear()
        driver.find_element_by_name("pureIncome").send_keys("40000")
        driver.find_element_by_name("pdIncome").clear()
        driver.find_element_by_name("pdIncome").send_keys("10000")
        driver.find_element_by_name("shiftIncome").clear()
        driver.find_element_by_name("shiftIncome").send_keys("20000")
        driver.find_element_by_name("lowGold").clear()
        driver.find_element_by_name("lowGold").send_keys("500")
        driver.find_element_by_name("liveGold").clear()
        driver.find_element_by_name("liveGold").send_keys("500")
        driver.find_element_by_name("otherIncome").clear()
        driver.find_element_by_name("otherIncome").send_keys("100")
        driver.find_element_by_name("pdPay").clear()
        driver.find_element_by_name("pdPay").send_keys("20")
        driver.find_element_by_name("personIncome").clear()
        driver.find_element_by_name("personIncome").send_keys("500")
        Select(driver.find_element_by_name("isOnlyChild")).select_by_visible_text(u"是")
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("usernameId").clear()
        driver.find_element_by_id("usernameId").send_keys(u"李四")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之女婿")
        driver.find_element_by_id("cardnoId").clear()
        driver.find_element_by_id("cardnoId").send_keys("610123198502101322")
        Select(driver.find_element_by_id("politicsId")).select_by_visible_text(u"中共党员")
        Select(driver.find_element_by_id("healthstatenameId")).select_by_visible_text(u"健康")
        Select(driver.find_element_by_id("workSkillId")).select_by_visible_text(u"普通劳动力")
        Select(driver.find_element_by_id("edustatenameId")).select_by_visible_text(u"小学")
        Select(driver.find_element_by_id("stustatenameId")).select_by_visible_text(u"高职三年级")
        Select(driver.find_element_by_id("laborstatenameId")).select_by_visible_text(u"乡（镇）内务工")
        Select(driver.find_element_by_id("nationalnameId")).select_by_visible_text(u"满族")
        driver.find_element_by_id("laborTimeId").clear()
        driver.find_element_by_id("laborTimeId").send_keys("2000")
        Select(driver.find_element_by_id("lifeStateId")).select_by_visible_text(u"正常")
        driver.find_element_by_id("switch-big1").click()
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"陈家坡村委会")
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_name("poorAttri")).select_by_visible_text(u"一般贫困户")
        # driver.find_element_by_css_selector("button.dialog-btn").click()
        # self.assertEqual(u"请添加家庭成员!", self.close_alert_and_get_its_text())
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_css_selector("td > button.dialog-btn").click()
        driver.find_element_by_link_text(u"删除").click()
        driver.find_element_by_css_selector("td > button.dialog-btn").click()
        driver.find_element_by_css_selector("input[type=\"radio\"]").click()
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之子")
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"张三")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按条件查找成员'张三'，统计的姓名为张三的成员总数为%d个" % int(value))
        driver.find_element_by_link_text("查看").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        time.sleep(3)
        driver.find_element_by_link_text(u"修改").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updFamilyId"))
        Select(driver.find_element_by_name("isInStu")).select_by_visible_text(u"否")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"保存成功!", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之子")
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"张三")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按条件查找成员'张三'，统计的姓名为张三的成员总数为%d个" % int(value))
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"成员删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此成员记录吗[\s\S]$")
        driver.find_element_by_link_text(u"成员删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此成员记录吗[\s\S]$")

        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之子")
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"张三")
        driver.find_element_by_id("queryBtn").click()

        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("删除按条件查找的成员'张三'后，统计的姓名为张三的成员总数为%d个"% int(value))
        time.sleep(5)
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之女婿")
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"李四")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按条件查找成员'李四'，统计的姓名为李四的成员总数为%d个" % int(value))
        driver.find_element_by_link_text("查看").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        time.sleep(5)
        driver.find_element_by_link_text(u"修改").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_updFamilyId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        Select(driver.find_element_by_name("isInStu")).select_by_visible_text(u"是")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"保存成功!", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之女婿")
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"李四")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按条件查找成员'李四'，统计的姓名为李四的成员总数为%d个" % int(value))
        self.accept_next_alert = False
        driver.find_element_by_link_text(u"成员删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此成员记录吗[\s\S]$")
        driver.find_element_by_link_text(u"成员删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确定删除此成员记录吗[\s\S]$")

        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之子")
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"张三")
        driver.find_element_by_id("queryBtn").click()

        value = driver.find_element_by_name("totalNum").get_attribute("value")
        print("删除按条件查找的成员'李四'后，统计的姓名为李四的成员总数为%d个" % int(value))
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
