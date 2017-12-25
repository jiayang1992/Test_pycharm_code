#coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,os,csv
import sys

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
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_id("userNameCopy").clear()
        driver.find_element_by_id("userNameCopy").send_keys("admin")
        driver.find_element_by_id("userPassword").clear()
        driver.find_element_by_id("userPassword").send_keys("666666")
        driver.find_element_by_id("btnLogin").click()
        driver.find_element_by_css_selector("li.unnum2").click()
        driver.find_element_by_id("second-01").click()
        driver.find_element_by_id("menu-sm0").click()
        driver.find_element_by_id("second-01").click()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_id("signedDay").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_xpath("/html/body/div[1]/iframe"))
        driver.find_element_by_xpath("/html/body/div/div[2]/table/tbody/tr[4]/td").click()
        driver.switch_to_default_content()
        driver.switch_to_frame(driver.find_element_by_class_name("iframeClass"))
        driver.find_element_by_css_selector("button.form-btn").click()
        #查看
        driver.find_element_by_xpath("/html/body/form/div[2]/table/tbody/tr[3]/td[5]/a").click()
        time.sleep(5)
        value = driver.find_element_by_id("signedDay").get_attribute("value")
        print("查询的考勤月份为%s月"%str(value))
        print("成功查看轨迹")
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_xpath("//*[@id='mainForm']/div[2]/table/tbody/tr[3]/td[6]/a").click()
        driver.find_element_by_name("dosubmit").click()
        time.sleep(3)
        print("成功查看日志")
        driver.find_element_by_xpath("//*[@id='mainForm']/div[2]/table/tbody/tr[3]/td[7]/div/a").click()
        time.sleep(2)
        print("成功导出数据")
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("departId")).select_by_visible_text("镇管办")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在部门'镇管办'查询到有%d条结果"%int(value2))
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("departId")).select_by_visible_text("全部")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在部门'全部'查询到有%d条结果" % int(value2))
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("departId")).select_by_visible_text("计育办")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在部门'计育办'查询到有%d条结果" % int(value2))
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("departId")).select_by_visible_text("镇管办")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在部门'镇管办'查询到有%d条结果" % int(value2))
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("departId")).select_by_visible_text("环卫")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在部门'环卫'查询到有%d条结果" % int(value2))
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("departId")).select_by_visible_text("财政所")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在部门'财政所'查询到有%d条结果" % int(value2))
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("areaId")).select_by_visible_text("全部")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在地区'全部'查询到有%d条结果" % int(value2))
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("areaId")).select_by_visible_text("镇川镇")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在地区'镇川镇'查询到有%d条结果" % int(value2))
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("areaId")).select_by_visible_text("西环路社区")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在地区'西环路社区'查询到有%d条结果" % int(value2))
        driver.find_element_by_id("resetBtn").click()
        Select(driver.find_element_by_name("areaId")).select_by_visible_text("南片区")
        driver.find_element_by_class_name("form-btn").click()
        value2 = driver.find_element_by_name("totalNum").get_attribute("value")
        print("按所在地区'南片区'查询到有%d条结果" % int(value2))
        driver.find_element_by_id("resetBtn").click()
        driver.find_element_by_xpath("//*[@id='resetBtn']").click()
        print("成功导出全部数据")
        driver.switch_to_default_content()
        driver.find_element_by_link_text(u"退出").click()
        # my_file = "C:\\Users\\admin\\Downloads\\考勤情况统计_20171215100646.csv"
        # data = csv.reader(open(my_file, "r"))
        # # user表示读取表中第一列名字，user表示读取表中第二列邮箱以此类推
        # for user in data:
        #     print(user[0])
        #     print(user[1])
        #     print(user[2])
        #     print(user[3])
    
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
