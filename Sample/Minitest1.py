#coding:utf-8
__author__ = 'a633335'

import unittest
from appium import webdriver
import time,os

class MyTests(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {
                'platformName': 'Android',
                'platformVersion': '9',
                'deviceName': 'a57c5aae',
                'appPackage': 'com.tencent.mm',
                'appActivity': 'com.tencent.mm.ui.LauncherUI',
                'automationName': 'Uiautomator2',
                # 'udid': 'a57c5aae',
                # 'resetKeyboard': True,
                'noReset': True,
               "automationName": "uiautomator2"
                }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    def test_miniprogram1(self, t=500):
        """页面下拉测试"""
        time.sleep(3)
        window = self.driver.get_window_size()
        x1 = window['width'] * 0.5  # 起始x坐标
        y1 = window['height'] * 0.2  # y1坐标，滑动起始点
        y2 = window['height'] * 0.7  # y2坐标，滑动末尾点
        self.driver.swipe(x1,y1,x1,y2,t) # 页面下拉
        self.driver.find_element_by_id('com.tencent.mm:id/ka').click() # 点击控件
        time.sleep(3)

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()