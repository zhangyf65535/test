#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 13:58
# @Author : zyf
# @File : login_page.py
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from page_locators.login_page_locator import LoginPageLocator as loc
from common.basepage import BasePage


class LoginPage(BasePage):

    def login(self, username, password):
        self.clear_text(loc.user_loc, "清除用户名信息")
        self.input_text(loc.user_loc, username, "登录页面_输入用户名")
        self.clear_text(loc.password_loc, "清除密码信息")
        self.input_text(loc.password_loc, password, "登录页面_输入密码")
        self.click_element(loc.login_button_loc, "登录页面_点击登录按钮")


    def get_form_error_info(self):
        return self.get_text(loc.form_error_loc_password, "The Password field is required.")

    def get_page_center_error_info(self):
        return self.get_text(loc.page_center_error_loc, "用户名/密码输入错误")