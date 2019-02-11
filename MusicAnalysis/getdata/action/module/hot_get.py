#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: hot_get.py
@time: 2019/2/10 17:41
"""
import re
from . import singers

# 核心算法：计算热度
class HotGet(object):

    # 判断是否是歌曲
    def choose_music(self, soup):
        couny_node = 0
        exist1 = soup.find('div', class_="op-musicsong c-row c-border")
        exist2 = soup.find(tpl="musicsongs")
        if exist1 is not None or exist2 is not None:
            couny_node += 1
        return couny_node

    # 判断是否是歌手
    def choose_singer(self, name):
        code = name in singers.singers
        return code

    # 计算热度
    def count_hot(self, soup):
        count_node = soup.find_all('a', class_="list")
        i = 0
        count = 0
        for li in count_node:
            i += 1
            count += int(re.findall("\\d+", li.get_text())[0])
        return count
