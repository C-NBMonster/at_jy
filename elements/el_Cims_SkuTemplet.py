#! /usr/bin/env python
#coding=utf-8

from selenium import webdriver

class CElement_mainPage(object):
    @staticmethod
    def element_mainPage_baseData():
        element = driver.find_element_by_link_text(u"基础数据系统")
        return element
    
    @staticmethod
    def element_mainPage_Pms():
        element = driver.find_element_by_link_text(u"商品系统")
        return element

    @staticmethod
    def element_mainPage_PURMS():
        element = driver.find_element_by_link_text(u"采购系统")
        return element

    @staticmethod
    def element_mainPage_WMS():
        element = driver.find_element_by_link_text(u"仓储系统")
        return element

    @staticmethod
    def element_mainPage_Oder():
        element = driver.find_element_by_link_text(u"订单系统")
        return element

    @staticmethod
    def element_mainPage_UC():
        element = driver.find_element_by_link_text(u"用户中心")
        return element

    @staticmethod
    def element_mainPage_PRMS():
        element = driver.find_element_by_link_text(u"促销中心")
        return element
    
    @staticmethod
    def element_mainPage_BI():
        element = driver.find_element_by_link_text(u"报表系统")
        return element
     