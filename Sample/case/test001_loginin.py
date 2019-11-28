#coding:utf-8
__author__ = 'a633335'

import unittest
from appium import webdriver
import time,os

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

    def test001_miniprogram_login(self, t=500):
        """账号密码登录小程序"""
        time.sleep(3)
        window = self.driver.get_window_size()
        x1 = window['width'] * 0.5  # 起始x坐标
        y1 = window['height'] * 0.2  # y1坐标，滑动起始点
        y2 = window['height'] * 0.7  # y2坐标，滑动末尾点
        self.driver.swipe(x1,y1,x1,y2,t) # 页面下拉
        time.sleep(2)
        self.driver.find_element_by_id('com.tencent.mm:id/ka').click() # 点击进入小程序
        time.sleep(2)
        add_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Button/android.view.View[3]/android.view.View[3]"
        self.driver.find_element_by_xpath(add_xpath).click()
        time.sleep(2)
        login1_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View"
        self.driver.find_element_by_xpath(login1_xpath).click()
        time.sleep(2)
        inputbox_account_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View"
        self.driver.find_element_by_xpath(inputbox_account_xpath).click()
        time.sleep(2)
        #点开数字键盘
        self.driver.tap([(230, 2023),(230, 2023)],100)
        time.sleep(2)
        self.driver.tap([(293, 1544)],100)#1([(293, 1544),(293, 1544)],100)
        time.sleep(1)
        self.driver.tap([(777, 1554)],100)#3([(777, 1554),(777, 1554)],100)
        time.sleep(1)
        self.driver.tap([(533, 1539)],100)#2([(533, 1539),(533, 1539)],100)
        time.sleep(1)
        self.driver.tap([(288, 1862)],100)#7([(288, 1862),(288, 1862)],100)
        time.sleep(1)
        self.driver.tap([(547, 2009)],100)#0([(547, 2009),(547, 2009)],100)
        time.sleep(1)
        self.driver.tap([(533, 1862)],100)#8([(533, 1862),(533, 1862)],100)
        time.sleep(1)
        self.driver.tap([(288, 1862)],100)#7([(288, 1862),(288, 1862)],100)
        time.sleep(1)
        self.driver.tap([(782, 1706)],100)#6([(782, 1706),(782, 1706)],100)
        time.sleep(1)
        self.driver.tap([(777, 1554)],100)#3([(777, 1554),(777, 1554)],100)
        time.sleep(1)
        self.driver.tap([(547, 2009)],100)#0([(547, 2009),(547, 2009)],100)
        time.sleep(1)
        self.driver.tap([(787, 1872)],100)#9([(787, 1872),(787, 1872)],100)
        time.sleep(1)
        inputbox_pwd_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View"
        self.driver.find_element_by_xpath(inputbox_pwd_xpath).click()
        time.sleep(4)
        self.driver.find_element_by_xpath(inputbox_pwd_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(inputbox_pwd_xpath).click()
        time.sleep(2)
        self.driver.tap([(59, 1544)],100)#q
        time.sleep(1)
        self.driver.tap([(166, 1554)],100)#w
        time.sleep(1)
        self.driver.tap([(274, 1544)],100)#e
        time.sleep(1)
        self.driver.tap([(376, 1549)],100)#r
        time.sleep(1)
        self.driver.tap([(220, 2023)],100)
        time.sleep(1)
        self.driver.tap([(288, 1549)],100)#1
        time.sleep(1)
        self.driver.tap([(542, 1549)],100)#2
        time.sleep(1)
        self.driver.tap([(777, 1554)],100)#3
        time.sleep(1)
        self.driver.tap([(303, 1706)],100)#4
        time.sleep(1)
        self.driver.tap([(88, 1539)],100)#.
        time.sleep(1)
        self.driver.tap([(547, 1139)],100)
        time.sleep(1)
        self.driver.tap([(518, 1569)],100)
        time.sleep(3)
        #注销
        #self.driver.tap([(933, 2023)],100)
        #time.sleep(3)
        #self.driver.swipe(500,1500,500,1000,500) # 页面上滑
        #time.sleep(2)
        #logout_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Button/android.view.View[1]/android.view.View/android.view.View[4]/android.view.View"
        #self.driver.find_element_by_xpath(logout_xpath).click()
        #time.sleep(3)
        #ha_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Button/android.view.View[3]/android.view.View[2]/android.view.View[3]/android.view.View[1]"
        #self.driver.find_element_by_xpath(ha_xpath).click()
        #time.sleep(3)
        #start_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Button/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View/android.view.View[2]"
        #self.driver.find_element_by_xpath(abort_xpath).click()
        #time.sleep(5)
        #self.driver.tap(718, 1319)
    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()