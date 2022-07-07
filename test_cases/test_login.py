#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 13:51
# @Author : zyf
# @File : test_login.py
from selenium import webdriver
import pytest
import time
from page_objects.login_page import LoginPage
from test_datas import login_datas as ld
from page_objects.index_page import IndexPage


@pytest.mark.usefixtures('init_driver')  # 表示调用init_driver的前置后置
class TestLogin:
    # 打上标记，将来想执行哪些用例就可以执行哪些用例
    @pytest.mark.smoke
    def test_login_success(self, init_driver): # fixture的函数名称，作为参数传给测试用例，函数名称=fixture返回的结果
        # 创建登录实例化对象，调用登录方法
        # init_driver == 之前的self.driver
        LoginPage(init_driver).login(ld.success_login["username"], ld.success_login["password"])
        time.sleep(3)
        # 创建实例化对象，判断是否登录成功
        assert IndexPage(init_driver).check_userName_exists()

