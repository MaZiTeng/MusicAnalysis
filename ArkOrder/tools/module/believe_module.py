#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: believe_module.py
@time: 2019/2/11 20:51
"""


class Believe(object):

    co = ["green", "red", "orange", "yellow", "purple", "blue"]

    def __init__(self, grade, nature, left, up, right, down):
        # 潜能
        self.grade = grade
        # 属性
        self.nature = nature
        # 四个方向指针
        self.left = Believe.co[left]
        self.up = Believe.co[up]
        self.right = Believe.co[right]
        self.down = Believe.co[down]
