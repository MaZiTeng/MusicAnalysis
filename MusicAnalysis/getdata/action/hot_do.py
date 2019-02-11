#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: hot_do.py
@time: 2019/2/10 12:23
"""

from .module import module, hot_get
from MusicAnalysis.getdata.action import html_parser
from .database import renewdb


class HotDo(object):
    def __init__(self):
        self.module = module.Module()
        self.hot = hot_get.HotGet()
        self.parser = html_parser.HtmlParser()
        self.renew = renewdb.RenewDatabase()

    def hot_do(self, name, wid):
        # 获取热度
        root_url = "http://music.taihe.com/search?key="
        # 组合url
        page_url = self.module.assemble_url(root_url, name)
        # 爬取数据
        soup = self.parser.parse(page_url)
        # 获取热度值
        hot = self.hot.count_hot(soup)
        # 将地址和热度写入数据库
        self.renew.renew_songs(wid, hot)
        # 还可以爬取很多参数
        return hot

    def judge_music(self, name):
        # 判断name是否是歌曲
        root_url = "http://www.baidu.com/baidu?wd="
        page_url = self.module.assemble_url(root_url, name, " 歌曲")
        soup = self.parser.parse(page_url)
        check_music = self.hot.choose_music(soup)
        if check_music is 0:
            print(name, "不是歌曲")
            return 0
        # 判断是否是歌手
        check_singer = self.hot.choose_singer(name)
        if check_singer is True:
            print(name, "是歌手")
            return 0
        return 1
