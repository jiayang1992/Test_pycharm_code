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
        Select(driver.find_element_by_id("villageId")).select_by_visible_text(u"八塌湾村委会")
        Select(driver.find_element_by_id("alterYearId")).select_by_visible_text(u"2015年度")
        Select(driver.find_element_by_id("poorAttriId")).select_by_visible_text(u"一般贫困户")
        Select(driver.find_element_by_id("identifyId")).select_by_visible_text(u"国家标准")
        Select(driver.find_element_by_id("leadResultId")).select_by_visible_text(u"因病")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        Select(driver.find_element_by_id("leadResultId")).select_by_visible_text(u"因病")
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"张")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("612721")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("6127211")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("6127211941")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("612721194")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("6127211943")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_xpath(u"//button[@value='导出']").click()
        Select(driver.find_element_by_id("isExistImgId")).select_by_visible_text(u"是")
        driver.find_element_by_id("queryBtn").click()
        Select(driver.find_element_by_id("isExistImgId")).select_by_visible_text(u"否")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"查看").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        driver.find_element_by_id("switch-big2").click()
        driver.find_element_by_link_text(u"有效").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_id("switch-big4").click()
        driver.find_element_by_id("switch-big5").click()
        # time.sleep(5)
        # driver.find_element_by_id("file-1").click()
        # os.system("uploadpicture.exe")
        # driver.find_element_by_xpath("//button[@type='button']").click()
        # driver.find_element_by_id("1516087924801955").clear()
        # driver.find_element_by_id("1516087924801955").send_keys("11")
        # driver.find_element_by_link_text(u"上传").click()
        # driver.find_element_by_id("1516087931509295").clear()
        # driver.find_element_by_id("1516087931509295").send_keys("11")
        # driver.find_element_by_xpath("//button[@type='button']").click()
        # driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        # driver.find_element_by_id("file-1").click()
        # os.system("uploadpicture.exe")
        # driver.find_element_by_link_text(u"上传").click()
        # driver.find_element_by_css_selector("button.save-btn").click()
        # driver.find_element_by_id("1516087958856694").clear()
        # driver.find_element_by_id("1516087958856694").send_keys("11")
        # driver.find_element_by_css_selector("button.save-btn").click()
        driver.find_element_by_id("switch-big6").click()
        # driver.find_element_by_xpath("(//input[@id='file-1'])[2]").click()
        # os.system("uploadpicture.exe")
        # driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        # driver.find_element_by_xpath("(//button[@type='button'])[4]").click()
        # driver.find_element_by_xpath("(//input[@id='file-1'])[2]").click()
        # os.system("uploadpicture.exe")
        # driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        # driver.find_element_by_id("1516087998855778").clear()
        # driver.find_element_by_id("1516087998855778").send_keys("12")
        # driver.find_element_by_css_selector("#imgForm02 > div.about-btnbg > ul.exam-ul > li > button.save-btn").click()
        # self.accept_next_alert = False
        # driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[2]").click()
        # self.assertEqual(u"删除后将无法恢复，确定要删除吗", self.close_alert_and_get_its_text())
        # driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[2]").click()
        # self.assertEqual(u"删除后将无法恢复，确定要删除吗", self.close_alert_and_get_its_text())
        # driver.find_element_by_id("switch-big5").click()
        # self.accept_next_alert = False
        # driver.find_element_by_link_text(u"删除").click()
        # self.assertEqual(u"删除后将无法恢复，确定要删除吗", self.close_alert_and_get_its_text())
        # driver.find_element_by_link_text(u"编辑").click()
        # driver.find_element_by_id("newImgName").clear()
        # driver.find_element_by_id("newImgName").send_keys("12")
        # driver.find_element_by_css_selector("input.save-btn").click()
        # driver.find_element_by_link_text(u"删除").click()
        # self.assertEqual(u"删除后将无法恢复，确定要删除吗", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_css_selector("input.dialog-btn").click()
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        time.sleep(5)
        driver.find_element_by_xpath(u"//button[@value='重置']").click()
        Select(driver.find_element_by_id("leadResultId")).select_by_visible_text(u"因病")
        driver.find_element_by_id("userNameId").clear()
        driver.find_element_by_id("userNameId").send_keys(u"张")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("612721")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("6127211")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("6127211941")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("612721194")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_id("cardNoId").clear()
        driver.find_element_by_id("cardNoId").send_keys("6127211943")
        driver.find_element_by_id("queryBtn").click()
        driver.find_element_by_link_text(u"查看").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_xpath(u"//input[@value='上一户']").click()
        driver.find_element_by_css_selector("input.dialog-btn").click()
        driver.find_element_by_xpath("//input[@id='closeId']").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        time.sleep(5)
        driver.find_element_by_id("310051768446").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_userId"))
        driver.find_element_by_xpath(u"//input[@value='下一户']").click()
        driver.find_element_by_xpath(u"//input[@value='上一户']").click()
        driver.find_element_by_css_selector("input.dialog-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_id("closeId").click()
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
