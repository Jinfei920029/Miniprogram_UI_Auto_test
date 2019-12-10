#coding:utf-8
__author__ = 'a633335'
import unittest
from appium import webdriver
import time,os

class Function:

    def isElementExist(self,element):
        #判断元素
        flag=True
        driver=self.driver
        try:
            driver.find_element_by_xpath(element)
            return flag
        except:
            flag=False
            return flag