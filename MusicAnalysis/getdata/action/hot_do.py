#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: hot_do.py
@time: 2019/2/10 12:23
"""
import re
from .module import module, hot_get
from MusicAnalysis.getdata.action import html_parser
from .database import renewdb


class HotDo(object):
    def __init__(self):
        self.module = module.Module()
        self.hot = hot_get.HotGet()
        self.parser = html_parser.HtmlParser()
        self.renew = renewdb.RenewDatabase()

    def hot_do(self, name, wid, hot_baidu):
        # 获取热度
        root_url1 = "http://music.taihe.com/search?key="                # 千千音乐
        root_url2 = "https://music.163.com/search/m/?s="              # 网易云音乐
        root_url3 = "https://www.xiami.com/search?key="                 # 虾米音乐
        root_url4 = "http://sou.kuwo.cn/ws/NSearch?type=all&catalog=yueku20177&key="   # 酷我音乐
        # 组合url
        page_url1 = self.module.assemble_url(root_url1, name)
        page_url2 = self.module.assemble_url(root_url2, name)
        page_url3 = self.module.assemble_url(root_url3, name)
        page_url4 = self.module.assemble_url(root_url4, name)
        # 爬取数据
        soup1 = self.parser.parse(page_url1)
        soup2 = self.parser.parse(page_url2)
        # soup3 = self.parser.parse(page_url3)
        soup4 = self.parser.parse(page_url4)
        # 获取热度值
        hot1 = self.hot.count_hot_qianqian(soup1)
        # hot2 = self.hot.count_hot_163(soup2)
        hot2 = 0
        # hot3 = self.hot.count_hot_xiami(soup3)
        hot3 = 0
        hot4 = self.hot.count_hot_kuwo(soup4)
        # 将地址和热度写入数据库
        self.renew.renew_songs(wid, hot1, hot_baidu, hot2, hot3, hot4)
        # 还可以爬取很多参数
        return hot1, hot2, hot3, hot4

    def judge_music(self, name):
        # 判断name是否是歌曲
        root_url = "http://www.baidu.com/baidu?wd="
        page_url = self.module.assemble_url(root_url, name, " 歌曲")
        soup = self.parser.parse(page_url)
        check_music = self.hot.choose_music(soup)
        hot_baidu = int(re.sub("[百度云为您找到相关结果约,，个]", "", soup.find('span', class_="nums_text").get_text()))
        if check_music is 0:
            print(name, "不是歌曲")
            return 0, hot_baidu
        # 判断是否是歌手
        check_singer = self.hot.choose_singer(name)
        if check_singer is True:
            print(name, "是歌手")
            return 0, hot_baidu
        return 1, hot_baidu
