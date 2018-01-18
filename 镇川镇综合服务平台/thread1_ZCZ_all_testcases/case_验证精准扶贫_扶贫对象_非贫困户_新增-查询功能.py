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
        driver.find_element_by_id("second-12").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath(u"//button[@value='新增']").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_addFamilyId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_name("isInStu")).select_by_visible_text(u"是")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("13265458945")
        driver.find_element_by_name("houseNum").clear()
        driver.find_element_by_name("houseNum").send_keys("4")
        driver.find_element_by_name("bankName").clear()
        driver.find_element_by_name("bankName").send_keys("6223561487912354621")
        driver.find_element_by_name("bankName").clear()
        driver.find_element_by_name("bankName").send_keys("")
        driver.find_element_by_name("bankNo").clear()
        driver.find_element_by_name("bankNo").send_keys("6223561487912354621")
        driver.find_element_by_name("bankName").clear()
        driver.find_element_by_name("bankName").send_keys(u"中国银行")
        driver.find_element_by_name("bankNo").clear()
        driver.find_element_by_name("bankNo").send_keys("23561487912354621")
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_id("usernameId").clear()
        driver.find_element_by_id("usernameId").send_keys(u"李小刚")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"配偶")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之子")
        driver.find_element_by_id("cardnoId").clear()
        driver.find_element_by_id("cardnoId").send_keys("627123198901231425")
        Select(driver.find_element_by_id("politicsId")).select_by_visible_text(u"中共党员")
        Select(driver.find_element_by_id("edustatenameId")).select_by_visible_text(u"高中")
        Select(driver.find_element_by_id("workSkillId")).select_by_visible_text(u"普通劳动力")
        Select(driver.find_element_by_id("nationalnameId")).select_by_visible_text(u"汉族")
        Select(driver.find_element_by_id("stustatenameId")).select_by_visible_text(u"大专及以上")
        Select(driver.find_element_by_id("edustatenameId")).select_by_visible_text(u"大专及以上")
        Select(driver.find_element_by_id("laborstatenameId")).select_by_visible_text(u"乡（镇）外县内务工")
        driver.find_element_by_id("laborTimeId").clear()
        driver.find_element_by_id("laborTimeId").send_keys("2400")
        Select(driver.find_element_by_id("lifeStateId")).select_by_visible_text(u"正常")
        driver.find_element_by_css_selector("td > button.dialog-btn").click()
        driver.find_element_by_id("switch-big3").click()
        Select(driver.find_element_by_name("isArtel")).select_by_visible_text(u"是")
        driver.find_element_by_name("gjArea").clear()
        driver.find_element_by_name("gjArea").send_keys("230")
        driver.find_element_by_name("tgArea").clear()
        driver.find_element_by_name("tgArea").send_keys("120")
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
        driver.find_element_by_name("distance").send_keys("2300")
        driver.find_element_by_name("houseArea").clear()
        driver.find_element_by_name("houseArea").send_keys("150")
        Select(driver.find_element_by_xpath("(//select[@name='isArtel'])[2]")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("fuelType")).select_by_visible_text(u"煤炭")
        Select(driver.find_element_by_name("fuelType")).select_by_visible_text(u"清洁能源")
        Select(driver.find_element_by_name("roadType")).select_by_visible_text(u"水泥路")
        Select(driver.find_element_by_name("houseLevel")).select_by_visible_text(u"A级")
        Select(driver.find_element_by_name("isToilet")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("isTv")).select_by_visible_text(u"是")
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_name("salaryIncome").clear()
        driver.find_element_by_name("salaryIncome").send_keys("50000")
        driver.find_element_by_name("estateIncome").clear()
        driver.find_element_by_name("estateIncome").send_keys("40000")
        driver.find_element_by_name("planGold").clear()
        driver.find_element_by_name("planGold").send_keys("0")
        driver.find_element_by_name("fiveGold").clear()
        driver.find_element_by_name("fiveGold").send_keys("0")
        driver.find_element_by_name("ecoGold").clear()
        driver.find_element_by_name("ecoGold").send_keys("0")
        driver.find_element_by_name("yearIncome").clear()
        driver.find_element_by_name("yearIncome").send_keys("50000")
        driver.find_element_by_name("salaryIncome").clear()
        driver.find_element_by_name("salaryIncome").send_keys("5000")
        driver.find_element_by_name("pureIncome").clear()
        driver.find_element_by_name("pureIncome").send_keys("40000")
        driver.find_element_by_name("pdIncome").clear()
        driver.find_element_by_name("pdIncome").send_keys("0")
        driver.find_element_by_name("shiftIncome").clear()
        driver.find_element_by_name("shiftIncome").send_keys("0")
        driver.find_element_by_name("lowGold").clear()
        driver.find_element_by_name("lowGold").send_keys("0")
        driver.find_element_by_name("liveGold").clear()
        driver.find_element_by_name("liveGold").send_keys("0")
        driver.find_element_by_name("otherIncome").clear()
        driver.find_element_by_name("otherIncome").send_keys("0")
        driver.find_element_by_name("pdPay").clear()
        driver.find_element_by_name("pdPay").send_keys("20000")
        driver.find_element_by_name("personIncome").clear()
        driver.find_element_by_name("personIncome").send_keys("3000")
        driver.find_element_by_id("switch-big5").click()
        Select(driver.find_element_by_name("isFamily")).select_by_visible_text(u"是")
        Select(driver.find_element_by_name("moveType")).select_by_visible_text(u"生态移民")
        Select(driver.find_element_by_name("moveMode")).select_by_visible_text(u"行政村整体搬迁")
        Select(driver.find_element_by_name("arrangeMode")).select_by_visible_text(u"购买商品房")
        Select(driver.find_element_by_name("arrangePlace")).select_by_visible_text(u"县城安置")
        Select(driver.find_element_by_name("moveDifficulty")).select_by_visible_text(u"搬迁后生活没着落")
        driver.find_element_by_css_selector("button.dialog-btn").click()
        self.assertEqual(u"保存成功！", self.close_alert_and_get_its_text())
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        if int(value) <= 0:
            print("新增失败，列表中没有显示新增的信息")
        else:
            print("新增成功，查询到%d个结果"%int(value))
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_id("houseReId")).select_by_visible_text(u"之子")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以所在村'八塌湾村委会'、与户主关系'之子'进行查询，查询到%d个结果"%int(value))
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("userNameId").send_keys("李小刚")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以贫困人口姓名'李小刚'进行查询，查询到%d个结果" % int(value))
        driver.find_element_by_xpath("//*[@id='familyUserFormId']/div[1]/ul/li[9]/button").click()
        print("导出成功")
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        driver.find_element_by_id("cardNoId").send_keys("61")
        driver.find_element_by_id("queryBtn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以身份证号码关键字'61'进行查询，查询到%d个结果" % int(value))
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
