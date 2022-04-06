'''
Author: your name
Date: 2022-04-01 10:36:41
LastEditTime: 2022-04-06 15:10:40
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \jsd2203d:\baidunetdiskdownload\tmooc_auto_sign_in\main_headless.py
'''
"""
使用selenium打开浏览器,进入达内慕课网
采用无头模式
"""
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

# 1.无头模式(无界面模式)打开浏览器
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)
# 2.在地址栏输入达内慕课网的URL地址
driver.get(url='https://www.tmooc.cn/')
# 3.点击右上角的登录按钮
driver.find_element_by_id('login_xxw').click()
# 4.输入账号
driver.find_element_by_id('js_account_pm').send_keys('')
# 5.输入密码
driver.find_element_by_id('js_password').send_keys('')
# 6.点登录
driver.find_element_by_id('js_submit_login').click()
# 7.切换browser到新的窗口，获取新窗口的对象
while True:
    sleep(1)
    if len(driver.window_handles) == 2:
        driver.switch_to.window(driver.window_handles[-1])
        break
# 8.新窗口点击签到
while True:
    sleep(1)
    try:
        driver.find_element_by_css_selector('#studyMsgUl .bbb1').click()
        break
    except NoSuchElementException:
        pass
    except ElementNotInteractableException:
        print('您可能已签到')
        break
# 9.获取签到结果
node = driver.find_element_by_css_selector('#studyMsgUl .wqd')
while True:
    sleep(1)
    if node.get_attribute('style') == 'display: block;':
        print('签到成功')
        break
# quit(): 关闭浏览器
driver.quit()
