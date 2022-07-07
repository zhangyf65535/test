#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 14:22
# @Author : zyf
# @File : index_page.py
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IndexPage:
    user_loc = (By.XPATH,'//a[contains(text(),"测试学校-张")]')

    # 通过导入WebDriver类，声明driver是WebDriver的对象，后面就会有智能提示
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def check_userName_exists(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.user_loc))
            return True
        except:
            return False