#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 14:31
# @Author : zyf
# @File : constant.py
import os

# 获取项目的根路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)
# 获取配置文件存放的路径
CONF_DIR = os.path.join(BASE_DIR,'conf')
# 获取日志存放的路径
LOG_DIR = os.path.join(BASE_DIR,'common')
# print(LOG_DIR)
# 获取数据存放的路径
DATA_DIR = os.path.join(BASE_DIR,'test_datas')
# 获取测试用例存放的路径
CASE_DIR = os.path.join(BASE_DIR,'test_cases')
# 获取图片存放的路径
IMG_DIR = os.path.join(BASE_DIR, 'outputs\imgs')
# 获取测试报告存放的路径
REPORT_DIR = os.path.join(BASE_DIR, r'outputs\reports')
# 获取测试报告存放的路径
ALLURE_REPORT_DIR = os.path.join(BASE_DIR, r'outputs\allure')
print(ALLURE_REPORT_DIR)