#!/usr/bin/env python
# encoding: utf-8


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: html_parser.py
@time: 未知
"""
from bs4 import BeautifulSoup
from .module import module

class HtmlParser(object):
    def __init__(self):
        self.module = module.Module()

    def parse(self, page_url):
        if page_url is None:
            return
        # 爬取url中的所有数据
        html_cont = self.module.download(page_url)
        # 整理数据成为soup
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

        return soup
