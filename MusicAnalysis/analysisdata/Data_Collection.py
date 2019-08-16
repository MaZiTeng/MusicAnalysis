#!/usr/bin/env python
# encoding: utf-8


"""
@python version: v3.8
@author: mzt
@software: PyCharm
@file: analysis_main.py
@time: 2019/8/16
"""

import numpy as np




class DataCollection(object):

    def collection(self):

        f = open("songs", "r")

        lines = f.readlines()
        # rows = len(lines)  # 文件行数

        datamat = np.zeros((4265, 7))  # 初始化矩阵

        row = 0
        for line in lines:
            if line[-2] != "\"":
                continue
            line = line[1:-2]
            line = line.strip().split('\",\"')
            datamat[row, 0] = line[0]
            datamat[row, 1:7] = line[2:8]
            row += 1

        f.close()
        # print(row)
        datamat = np.delete(datamat, -2, 1)
        datamat = np.delete(datamat, -2, 1)
        # print(datamat)

        return datamat


