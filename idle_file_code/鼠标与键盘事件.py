#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,os
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
option = webdriver.ChromeOptions()
executable_path = 'C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe'
os.environ['webdriver.chrome.driver'] = executable_path
driver = webdriver.Chrome(executable_path,chrome_options=option)

driver.get("https://www.baidu.com/")
#from selenium.webdriver.common.keys import Keys 在使用键盘按键方法前需要先导入keys类包。
# 下面经常使用到的键盘操作：
# send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
# send_keys(Keys.SPACE) 空格键(Space)
# send_keys(Keys.TAB) 制表键(Tab)
# send_keys(Keys.ESCAPE) 回退键（Esc）
# send_keys(Keys.ENTER) 回车键（Enter）
# send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
# send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
# send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
# send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
time.sleep(3)

#定位到要右击的元素
# ActionChains 类鼠标操作的常用方法：
# context_click() 右击
# double_click() 双击
# drag_and_drop() 拖动
# move_to_element() 鼠标悬停在一个元素上
# click_and_hold() 按下鼠标左键在一个元素上
#click_and_hold(left)按下鼠标左键
#ActionChains 用于生成用户的行为；所有的行为都存储在 actionchains 对象。通过 perform()执行存储的行为。

#对定位到的元素执行鼠标右键操作
qqq =driver.find_element_by_id("kw")
ActionChains(driver).context_click(qqq).perform()
time.sleep(3)
