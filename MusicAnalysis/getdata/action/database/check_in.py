#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: check_in.py
@time: 2019/2/9 10:18
"""
import pymysql


class CheckDatabase(object):
    def __init__(self):
        self.url = "localhost"
        self.username = "root"
        self.password = ""
        self.database = "bigdata"

    def ConnectDB(self):
        db = pymysql.connect(self.url, self.username, self.password, self.database)
        return db

    def check_in(self, name):
        if name is None:
            return None

        check = 0
        uid = None

        db = self.ConnectDB()
        cursor = db.cursor()
        sql = "SELECT * FROM `songs` WHERE name = '%s'" % name
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取记录
            results = cursor.fetchone()
            if results is not None:
                check = 1
                uid = results[0]
        except:
            print("Error: check_in.check_in error")

        db.close()
        return check, uid
