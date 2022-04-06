'''
Author: your name
Date: 2022-04-01 10:36:41
LastEditTime: 2022-04-06 15:09:44
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \jsd2203d:\baidunetdiskdownload\tmooc_auto_sign_in\main.py
'''
"""
使用selenium打开浏览器,进入达内慕课网自动签到
"""
import sys
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException


def main(driver):
    # 2.在地址栏输入达内慕课网的URL地址
    while True:
        try:
            driver.get(url='https://www.tmooc.cn/')
            break
        except Exception as e:
            print(e)
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
    # 8.日志文件
    f = open('tts.txt','w+')
    # 9.新窗口点击签到
    while True:
        sleep(1)
        try:
            driver.find_element_by_css_selector('#studyMsgUl .bbb1').click()
            break
        except NoSuchElementException:
            pass
        except ElementNotInteractableException:
            f.write('您可能已签到')
            break
    # 11.获取签到结果
    node = driver.find_element_by_css_selector('#studyMsgUl .wqd')
    while True:
        sleep(1)
        if node.get_attribute('style') == 'display: block;':
            f.write('签到成功')
            break
"""     

    while True:
        sleep(3)
        try:
            driver.get(url='https://tts.tmooc.cn/studentCenter/studentSign?studentClaId=941611')
            break
        except Exception as e:
            print(e)
"""

if __name__ == '__main__':
    # 1.打开浏览器 - 创建浏览器对象
    driver = webdriver.Chrome()
    # 浏览器窗口最大化
    driver.maximize_window()
    try:
        main(driver)
    except Exception as e:
        print(e)

    driver.quit()
