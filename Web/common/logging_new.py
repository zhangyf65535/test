#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 14:30
# @Author : zyf
# @File : logging_new.py
import logging
import os
from common.constant import LOG_DIR
# from common.py0815_conf import conf


class MyLogging(object):
    def __new__(cls, *args, **kwargs):
        # 创建自己的日志收集器，用来收集日志信息
        my_log = logging.getLogger('my_log')
        my_log.setLevel('DEBUG')
        # 创建一个输出渠道（输出到控制台）
        l_s = logging.StreamHandler()
        l_s.setLevel('WARNING')
        # 创建一个日志输出渠道（输出到文件中）
        # log = conf.get('log', 'log_name')
        # log = log.log
        l_f = logging.FileHandler(os.path.join(LOG_DIR, "log.log"), encoding='utf8')
        l_f.setLevel('DEBUG')
        # 将输出渠道添加到日志收集器中
        my_log.addHandler(l_s)
        my_log.addHandler(l_f)

        # 设置日志输出格式
        ft = '%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s'
        ft = logging.Formatter(ft)
        # 设置日志输出格式
        l_s.setFormatter(ft)
        l_f.setFormatter(ft)

        return my_log

m_log = MyLogging()