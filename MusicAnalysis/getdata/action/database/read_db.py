#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: read_db.py
@time: 2019/2/8 21:42
"""
import pymysql


class ReadDatabase(object):
    def __init__(self):
        self.url = "localhost"
        self.username = "root"
        self.password = ""
        self.database = "healing2018"

    def ConnectDB(self):
        db = pymysql.connect(self.url, self.username, self.password, self.database)
        return db

    def read_songs_name(self, aid):
        if aid is None:
            return None

        name = 0

        db = self.ConnectDB()
        cursor = db.cursor()
        sql = "SELECT * FROM `songs` WHERE id = %s" % aid
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取记录
            results = cursor.fetchone()
            # 若id为空判断
            if results is not None:
                name = results[2]
        except:
            print("Error: read_db.read_songs_name error")

        db.close()
        return name
