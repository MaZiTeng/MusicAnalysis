#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: create.py
@time: 2019/2/8 22:46
"""
import pymysql


class CreateRecords(object):
    def __init__(self):
        self.url = "localhost"
        self.username = "root"
        self.password = ""
        self.database = "bigdata"

    def ConnectDB(self):
        db = pymysql.connect(self.url, self.username, self.password, self.database)
        return db

    def create_records(self, name):
        if name is None:
            return None

        last_id = None

        db = self.ConnectDB()
        cursor = db.cursor()
        sql = "INSERT INTO `songs` (`name`) VALUES ('%s')" % name
        try:
            # 执行sql语句
            cursor.execute(sql)
            last_id = db.insert_id()
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
            print("Error: create.create_records error")

        db.close()
        return last_id
