#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2022/7/5 14:00
# @Author : zyf
# @File : basepage.py
from common.logging_new import m_log
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from common.constant import IMG_DIR
from page_locators.login_page_locator import LoginPageLocator as loc


class BasePage:
    # 通过导入WebDriver类，声明driver是WebDriver的对象，后面就会有智能提示
    def __init__(self, driver: WebDriver):
        self.driver = driver
    # 等待元素可见
    def wait_ele_visible(self, loc, img_desc, timout=30, frequency=0.5):
        try:
            WebDriverWait(self.driver, timout, frequency).until(EC.visibility_of_element_located(loc))
        except:
            # 记录错误日志
            m_log.exception(f"等待元素{loc}可见失败！")
            # 截图
            self.save_img(img_desc)
            raise  # 抛出异常，让用例识别到异常将用例状态改为失败
        else:
            m_log.info(f"等待元素{loc}可见成功！")

    # 截图
    def save_img(self, img_description):
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        file_path = f"{img_description}_{now}.png"
        img_path = os.path.join(IMG_DIR, file_path)
        try:
            self.driver.save_screenshot(img_path)
        except:
            m_log.exception("网页截图失败！")
        else:
            m_log.info(f"截图成功，截图存放在：{img_path}！")

    def get_element(self, loc, img_desc):
        try:
            ele = self.driver.find_element(*loc)
        except:
            # 日志
            m_log.exception(f"查找{img_desc}元素{loc}失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            m_log.info(f"查找{img_desc}元素{loc}成功！")
            return ele

    def click_element(self, loc, img_desc, timout=30, frequency=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_desc, timout, frequency)
        # 查找元素
        ele = self.get_element(loc, img_desc)
        # 操作
        try:
            ele.click()
            m_log.info(f"点击{img_desc}元素{loc}成功！")
        except:
            # 日志
            m_log.exception(f"点击{img_desc}元素{loc}失败！")
            # 截图
            self.save_img(img_desc)
            raise

    def input_text(self, loc, value, img_desc, timout=30, frequency=0.5):
        # 等待元素可见
        self.wait_ele_visible(loc, img_desc, timout, frequency)
        # 查找元素
        ele = self.get_element(loc, img_desc)
        # 操作
        try:
            ele.send_keys(value)
            m_log.info(f"在{img_desc}元素{loc}上输入文本值: {value}成功！")
        except:
            # 日志
            m_log.info(f"在{img_desc}元素{loc}上输入文本值: {value}失败！")
            # 截图
            self.save_img(img_desc)
            raise

    def get_text(self, loc, img_desc, timout=30, frequency=0.5):
        # 等待元素存在
        self.wait_ele_visible(loc, img_desc, timout, frequency)
        # 查找元素
        ele = self.get_element(loc, img_desc)
        # 操作
        try:
            text = ele.text
            m_log.info(f"在{img_desc}元素{loc}获取文本值成功！")
        except:
            # 日志
            m_log.info(f"在{img_desc}元素{loc}获取文本值失败！")
            # 截图
            self.save_img(img_desc)
            raise
        else:
            return text

    def clear_text(self, loc, img_desc, timout=30, frequency=0.5):
        # 等待元素存在
        self.wait_ele_visible(loc, img_desc, timout, frequency)
        # 查找元素
        ele = self.get_element(loc, img_desc)
        # 操作
        try:
            ele.clear()
            m_log.info(f"在{img_desc}元素{loc}清除文本值成功！")
        except:
            # 日志
            m_log.info(f"在{img_desc}元素{loc}清除失败！")
            # 截图
            self.save_img(img_desc)
            raise