#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 15:11
# @Author : zyf
# @File : conftest.py
from selenium import webdriver
# 将数据从专门存放数据的文件中导入
from test_datas import common_datas as cd
import pytest
from page_objects.login_page import LoginPage
from test_datas import login_datas as ld


# 声明它之下的函数是一个pytest的前置后置（默认函数级别，可以设置为类/模块/会话级别）
# fixture函数中默认参数是scope=function，还可以是class/module/session
@pytest.fixture
def init_driver():
    # 前置
    driver = webdriver.Chrome()
    driver.get(cd.login_url)
    driver.maximize_window()
    yield driver  # 1.隔开前置后置；2.代替return返回driver(在这里不能用return返回)
    # 后置
    driver.quit()

# 如果前置后置跟之前的前置后置有重复的，可以类似于继承之前的函数中的前置后置，节省代码
@pytest.fixture
def login_web(init_driver):  # 调用并且也代表返回值(跟之前一样的前置就不需要再写了)
    LoginPage(init_driver).login(ld.success_login["username"], ld.success_login["password"])
    yield init_driver
"""   
执行的先后顺序，
先执行init_driver的前置，
再执行login_web的前置，
然后再执行login_web的后置，
最后执行init_driver的后置
"""






# @pytest.fixture(scope="class")
# def myFix():
#     print("===我是一个类级别的===前置===")
#     yield
#     print("===我是一个类级别的===后置===")


# 针对整个目录下的用例，用例是有执行先后顺序的，如果将这个放到后面的用例上，则前面的用例则不会调用
# @pytest.fixture(scope="module")
# def myMod():
#     print("===我是一个模块级别的===前置===")
#     yield
#     print("===我是一个模块级别的===后置===")


# 只有在会话级别的时候，才建议将autouse默认改为True，其他情况不建议直接调用前置后置
# @pytest.fixture(scope="session",autouse=True)
# def myMod():
#     print("===我是一个会话级别的===前置===")
#     yield
#     print("===我是一个会话级别的===后置===")

