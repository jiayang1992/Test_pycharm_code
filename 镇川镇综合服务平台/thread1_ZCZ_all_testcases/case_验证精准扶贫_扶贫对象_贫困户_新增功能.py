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
        driver.find_element_by_css_selector("li.unnum4").click()
        driver.find_element_by_id("menu-sm1").click()
        driver.find_element_by_id("second-10").click()
        driver.find_element_by_id("menuli00").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath(u"//button[@value='新增']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addFamilyId"))
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath(u"//button[@value='新增']").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addFamilyId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_name("leadResult")).select_by_visible_text(u"因病")
        Select(driver.find_element_by_name("otherResult")).select_by_visible_text(u"因病")
        Select(driver.find_element_by_name("isSoldierFamily")).select_by_visible_text(u"是")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("13285764512")
        Select(driver.find_element_by_name("poorAttri")).select_by_visible_text(u"一般贫困户")
        driver.find_element_by_name("houseNum").clear()
        driver.find_element_by_name("houseNum").send_keys("5")
        driver.find_element_by_name("bankName").clear()
        driver.find_element_by_name("bankName").send_keys("627015467891235")
        driver.find_element_by_name("bankName").clear()
        driver.find_element_by_name("bankName").send_keys("")
        driver.find_element_by_name("bankNo").clear()
        driver.find_element_by_name("bankNo").send_keys("627015467891235")
        driver.find_element_by_name("bankName").clear()
        driver.find_element_by_name("bankName").send_keys(u"中国农行")
        driver.find_element_by_name("helpNeed").clear()
        driver.find_element_by_name("helpNeed").send_keys(u"无")
        driver.find_element_by_name("bankNo").clear()
        driver.find_element_by_name("bankNo").send_keys("62701546789123")
        driver.find_element_by_name("bankNo").clear()
        driver.find_element_by_name("bankNo").send_keys("627015467891")
        Select(driver.find_element_by_name("tpAttri")).select_by_visible_text(u"未脱贫")
        Select(driver.find_element_by_name("alterType")).select_by_visible_text(u"家庭成员信息变更")
        driver.find_element_by_id("alterTime").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addFamilyId"))
        driver.find_element_by_name("alterReason").clear()
        driver.find_element_by_name("alterReason").send_keys(u"无")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big1").click()
        driver.find_element_by_name("bankNo").clear()
        driver.find_element_by_name("bankNo").send_keys("627015467891235")
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("usernameId").clear()
        driver.find_element_by_id("usernameId").send_keys(u"张泽丽")
        driver.find_element_by_id("cardnoId").clear()
        driver.find_element_by_id("cardnoId").send_keys("627120198706211522")
        Select(driver.find_element_by_id("politicsId")).select_by_visible_text(u"中共党员")
        Select(driver.find_element_by_id("edustatenameId")).select_by_visible_text(u"高中")
        Select(driver.find_element_by_id("workSkillId")).select_by_visible_text(u"普通劳动力")
        Select(driver.find_element_by_id("workSkillId")).select_by_visible_text(u"技能劳动力")
        Select(driver.find_element_by_id("nationalnameId")).select_by_visible_text(u"汉族")
        Select(driver.find_element_by_id("stustatenameId")).select_by_visible_text(u"非在校生")
        Select(driver.find_element_by_id("laborstatenameId")).select_by_visible_text(u"乡（镇）内务工")
        driver.find_element_by_id("laborTimeId").clear()
        driver.find_element_by_id("laborTimeId").send_keys("1200")
        Select(driver.find_element_by_id("lifeStateId")).select_by_visible_text(u"户清退时清退人员")
        Select(driver.find_element_by_id("lifeStateId")).select_by_visible_text(u"正常")
        driver.find_element_by_css_selector("td > button.dialog-btn").click()
        driver.find_element_by_link_text(u"删除").click()
        driver.find_element_by_css_selector("td > button.dialog-btn").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_name("gjArea").clear()
        driver.find_element_by_name("gjArea").send_keys("120")
        driver.find_element_by_name("tgArea").clear()
        driver.find_element_by_name("tgArea").send_keys("30")
        driver.find_element_by_name("mcArea").clear()
        driver.find_element_by_name("mcArea").send_keys("50")
        Select(driver.find_element_by_name("isElecPro")).select_by_visible_text(u"是")
        driver.find_element_by_name("gdArea").clear()
        driver.find_element_by_name("gdArea").send_keys("50")
        driver.find_element_by_name("ldArea").clear()
        driver.find_element_by_name("ldArea").send_keys("0")
        driver.find_element_by_name("lgArea").clear()
        driver.find_element_by_name("lgArea").send_keys("0")
        driver.find_element_by_name("smArea").clear()
        driver.find_element_by_name("smArea").send_keys("0")
        driver.find_element_by_name("distance").clear()
        driver.find_element_by_name("distance").send_keys("2200")
        driver.find_element_by_name("houseArea").clear()
        driver.find_element_by_name("houseArea").send_keys("120")
        Select(driver.find_element_by_name("isWaterDiff")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("isHouse")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("fuelType")).select_by_visible_text(u"柴草")
        Select(driver.find_element_by_name("isElce")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("roadType")).select_by_visible_text(u"泥土路")
        Select(driver.find_element_by_name("isWaterSafe")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("houseLevel")).select_by_visible_text(u"B级")
        Select(driver.find_element_by_name("isToilet")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("isTv")).select_by_visible_text(u"是")
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_name("salaryIncome").clear()
        driver.find_element_by_name("salaryIncome").send_keys("1200")
        driver.find_element_by_name("estateIncome").clear()
        driver.find_element_by_name("estateIncome").send_keys("1200")
        driver.find_element_by_name("planGold").clear()
        driver.find_element_by_name("planGold").send_keys("200")
        driver.find_element_by_name("fiveGold").clear()
        driver.find_element_by_name("fiveGold").send_keys("1000")
        driver.find_element_by_name("ecoGold").clear()
        driver.find_element_by_name("ecoGold").send_keys("0")
        driver.find_element_by_name("yearIncome").clear()
        driver.find_element_by_name("yearIncome").send_keys("30000")
        driver.find_element_by_name("pureIncome").clear()
        driver.find_element_by_name("pureIncome").send_keys("28000")
        driver.find_element_by_name("pdIncome").clear()
        driver.find_element_by_name("pdIncome").send_keys("12000")
        driver.find_element_by_name("shiftIncome").clear()
        driver.find_element_by_name("shiftIncome").send_keys("0")
        driver.find_element_by_name("lowGold").clear()
        driver.find_element_by_name("lowGold").send_keys("5000")
        driver.find_element_by_name("liveGold").clear()
        driver.find_element_by_name("liveGold").send_keys("5000")
        driver.find_element_by_name("otherIncome").clear()
        driver.find_element_by_name("otherIncome").send_keys("0")
        driver.find_element_by_name("pdPay").clear()
        driver.find_element_by_name("pdPay").send_keys("5000")
        driver.find_element_by_name("personIncome").clear()
        driver.find_element_by_name("personIncome").send_keys("6000")
        Select(driver.find_element_by_name("isOnlyChild")).select_by_visible_text(u"是")
        driver.find_element_by_id("switch-big5").click()
        driver.find_element_by_id("switch-big4").click()
        Select(driver.find_element_by_name("isTwoChild")).select_by_visible_text(u"是")
        driver.find_element_by_id("switch-big5").click()
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"张泽丽")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"查看").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_id("switch-big5").click()
        driver.find_element_by_id("switch-big6").click()
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_css_selector("input.dialog-btn").click()
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        time.sleep(3)
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
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
