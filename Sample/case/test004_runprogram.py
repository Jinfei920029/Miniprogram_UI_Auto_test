#coding:utf-8
__author__ = 'a633335'

import unittest
from appium import webdriver
import time,os
from Sample.Function.common import *

class MyTests(unittest.TestCase):
    # 测试开始前执行的方法，测试开始前的准备
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

    def test004_ha_control(self, t=500):
        """家电控制测试"""
        time.sleep(3)
        window = self.driver.get_window_size()
        x1 = window['width'] * 0.5  # 起始x坐标
        y1 = window['height'] * 0.2  # y1坐标，滑动起始点
        y2 = window['height'] * 0.7  # y2坐标，滑动末尾点
        self.driver.swipe(x1,y1,x1,y2,t) # 页面下拉
        self.driver.find_element_by_id('com.tencent.mm:id/ka').click() # 点击进入小程序
        time.sleep(2)
        ha_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Button/android.view.View[3]/android.view.View[2]/android.view.View[3]/android.view.View[1]"
        self.driver.find_element_by_xpath(ha_xpath).click()
        time.sleep(3)
        start_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Button/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[2]"
        self.driver.find_element_by_xpath(start_xpath).click()
        time.sleep(5)
        '''abort_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Button/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[2]"
        self.driver.find_element_by_xpath(abort_xpath).click()
        time.sleep(5)
        self.driver.tap([(718, 1319),(718, 1319)],100)'''
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()