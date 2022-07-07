#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 14:41
# @Author : zyf
# @File : pytest_main.py
import pytest
from common.constant import REPORT_DIR
from common.constant import ALLURE_REPORT_DIR
import os
import allure_pytest
import allure

# -s和-v显示执行用例的详细信息，-m用来执行带标记的用例
report_path = os.path.join(REPORT_DIR, 'pytest.html')
# allure_report_pat = os.path.join(ALLURE_REPORT_DIR, 'pytest.html')
if __name__ == '__main__':
    # pytest.main(["-s","-v","-m","smoke",f"--html={report_path}"])
    pytest.main([f"--html={report_path}", f"--alluredir={ALLURE_REPORT_DIR}"])