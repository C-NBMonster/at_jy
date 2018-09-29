# coding = utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_18.py
@time: 2018/9/29 14:29
@desc: 小问卷
"""


from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_18():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder18_Questionnaire_Title(self, driver):
        """问卷标题"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "top_tab_center_title"))
        return el

    def el_NewOrder18_Question_1(self, driver):
        """问题1，以前借贷次数"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_time"))
        return el

    def el_NewOrder18_Question_2(self, driver):
        """问题2，从哪里获知即有宝"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose"))
        return els

    def el_NewOrder18_Submit(self, driver):
        """提交"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_questionnaire_next"))
        return el


