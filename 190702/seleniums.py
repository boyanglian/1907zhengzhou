from selenium import webdriver
import time
# 后面是你的浏览器驱动位置，记得前面加r''，'r'是防止字符转义的
wd = webdriver.Chrome()
wd.get("https://www.taobao.com")    # 打开百度浏览器
wd.find_elements_by_id("kw").send_keys("lv")   # 定位输入框并输入关键字
wd.find_elements_by_id("su").click()   #点击[百度一下]搜索
time.sleep(3)   #等待3秒
# wd.quit()   #关闭浏览器