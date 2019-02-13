#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: main.py
@time: 2019/2/11 20:19
"""
from ArkOrder.tools.module import believe_maker


class DoCount(object):
    def __init__(self):
        self.believe_maker = believe_maker.believes

    def count(self):

        print("ok")

if __name__ == "__main__":

    ask = DoCount()
    ask.count()
