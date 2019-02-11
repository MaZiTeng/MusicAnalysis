#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: module.py
@time: 2019/2/10 17:31
"""
import urllib.parse
import re
import urllib.request



class Module(object):

    # 组装url
    def assemble_url(self, head, tail, add=""):
        if head is None or tail is None:
            return
        # url编码并组合
        return head + urllib.parse.quote(tail) + urllib.parse.quote(add)
        # url解码方式：urllib.parse.unquote(url)

    # 清洗名字
    def wash_data(self, music_name):
        # print("清洗这个名字")
        music_name = re.sub('\(.*?\)', "", music_name)
        music_name = re.sub('（.*?）', "", music_name)
        music_name = re.sub(r'-.*$', "", music_name)
        music_name = re.sub('[^\s\w\u4e00-\u9fff]+', "", music_name)
        # print(name)
        return music_name

    # 下载url
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
