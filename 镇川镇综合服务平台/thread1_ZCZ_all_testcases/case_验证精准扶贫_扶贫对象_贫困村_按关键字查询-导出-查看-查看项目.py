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
        driver.find_element_by_id("second-11").click()
        driver.find_element_by_id("menuli01").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        print("以村名称关键字'八'进行搜索：")
        driver.find_element_by_name("villageName").clear()
        driver.find_element_by_name("villageName").send_keys(u"八")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以村名称关键字'八'进行搜索，搜索到%d条信息"%int(value))
        driver.find_element_by_xpath("//button[@type='button']").click()
        print("以村负责人关键字'张'进行搜索：")
        driver.find_element_by_name("villager").clear()
        driver.find_element_by_name("villager").send_keys(u"张")
        driver.find_element_by_css_selector("button.form-btn").click()
        value = driver.find_element_by_id("totalNum").get_attribute("value")
        print("以村负责人关键字'张'进行搜索，搜索到%d条信息" % int(value))
        driver.find_element_by_xpath("//button[@type='button']").click()
        print("成功重置")
        print("以村负责人关键字'张冬生'进行搜索：")
        driver.find_element_by_name("villager").clear()
        driver.find_element_by_name("villager").send_keys(u"张冬生")
        driver.find_element_by_css_selector("button.form-btn").click()
        print("以村负责人关键字'张冬生'进行搜索，搜索到%d条信息" % int(value))
        # driver.find_element_by_xpath("//button[@type='button']").click()
        print("查看张冬生所在村信息")
        driver.find_element_by_id("610802028010").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_villageId"))
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        print("查看‘基本信息’：")
        driver.find_element_by_id("switch-big1").click()
        print("查看‘土地信息’：")
        driver.find_element_by_id("switch-big2").click()
        print("查看‘人口信息’：")
        driver.find_element_by_id("switch-big3").click()
        print("查看‘收入信息’：")
        driver.find_element_by_id("switch-big4").click()
        print("查看‘社会保障信息’：")
        driver.find_element_by_id("switch-big5").click()
        print("查看‘村级道路畅通’：")
        driver.find_element_by_id("switch-big6").click()
        print("查看‘饮水安全’：")
        driver.find_element_by_id("switch-big7").click()
        print("查看‘农村电力保障’：")
        driver.find_element_by_id("switch-big8").click()
        print("查看‘特色产业增收’：")
        driver.find_element_by_id("switch-big9").click()
        print("查看‘乡村旅游’：")
        driver.find_element_by_id("switch-big10").click()
        print("查看‘卫生和计划生育’：")
        driver.find_element_by_id("switch-big11").click()
        print("查看‘文化建设’：")
        driver.find_element_by_id("switch-big12").click()
        print("查看‘贫困村信息化’：")
        driver.find_element_by_id("switch-big13").click()
        print("查看‘驻村工作队’：")
        driver.find_element_by_id("switch-big14").click()
        print("查看‘驻村第一书记’：")
        driver.find_element_by_id("switch-big17").click()
        print("查看‘帮扶措施’：")
        driver.find_element_by_id("switch-big15").click()
        print("查看‘受益项目’：")
        driver.find_element_by_id("switch-big18").click()
        driver.find_element_by_id("5700000005855270").click()
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_projectId"))
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_villageId"))
        driver.find_element_by_id("closeId").click()
        time.sleep(3)
        print("查看‘村庄全景图’：")
        driver.find_element_by_id("switch-big16").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("closeId").click()
        time.sleep(5)
        print("查看张冬生所在村项目：")
        driver.find_element_by_link_text(u"查看项目").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_villageId"))
        driver.find_element_by_id("5700000005855270").click()
        driver.find_element_by_id("closeId").click()
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.switch_to_frame(driver.find_element_by_id("atrDialogIframe_villageId"))
        driver.find_element_by_id("switch-big1").click()
        driver.find_element_by_id("switch-big3").click()
        driver.find_element_by_css_selector("input.dialog-btn").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        print("成功查看！")
        time.sleep(3)
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_xpath(u"//button[@value='导出']").click()
        print("成功导出！")
        driver.find_element_by_xpath("//button[@type='button']").click()
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
