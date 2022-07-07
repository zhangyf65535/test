#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 14:04
# @Author : zyf
# @File : login_page_locator.py
from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 定义成类属性，方便后期维护(将定位的元素与页面对象分离)
    # 用户输入框
    user_loc = (By.XPATH, '//input[@class="ant-input" and @placeholder="请输入账号"]')
    # 密码输入框
    password_loc = (By.XPATH, '//input[@class="ant-input" and @placeholder="请输入密码"]')
    # 登录按钮
    login_button_loc = (By.XPATH, '//button[@class="login-form-button btn_active"]')
    # 账号为空
    form_error_loc_username = (By.XPATH, '//li[contains(text(),"The Username field is required.")]')
    # 密码为空
    form_error_loc_password = (By.XPATH, '//li[contains(text(),"The Password field is required.")]')
    # 账号或者密码错误信息提示
    page_center_error_loc = (By.XPATH, '//div[@class="layui-layer-content"]')