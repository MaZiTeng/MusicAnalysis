#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: renewdb.py
@time: 2019/2/8 23:47
"""
import pymysql


class RenewDatabase(object):
    def __init__(self):
        self.url = "localhost"
        self.username = "root"
        self.password = ""
        self.database = "bigdata"

    def ConnectDB(self):
        db = pymysql.connect(self.url, self.username, self.password, self.database)
        return db

    def renew_songs(self, wid, hot1, hot_baidu, hot2, hot3, hot4):
        if wid is None:
            return None
        db = self.ConnectDB()
        cursor = db.cursor()
        # SQL 更新语句
        sql = "UPDATE `songs` SET `hot_qianqian` = '%s', `hot_baidu` = '%s', `hot_163` = '%s', `hot_xiami` = '%s'," \
              " `hot_kuwo` = '%s' WHERE `songs`.`id` = %s" % (hot1, hot_baidu, hot2, hot3, hot4, wid)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
        db.close()
        return

    def renew_count(self, wid):
        if wid is None:
            return None

        count = 1

        db = self.ConnectDB()
        cursor = db.cursor()
        sql_get = "SELECT * FROM `songs` WHERE id = %s" % wid
        try:
            # 执行SQL语句
            cursor.execute(sql_get)
            # 获取记录
            results = cursor.fetchone()
            count = results[2]
        except:
            print("Error: renewdb.renew_count.get error")

        count += 1

        sql_updata = "UPDATE `songs` SET `count` = '%s' WHERE `songs`.`id` = %s " % (count, wid)
        try:
            # 执行SQL语句
            cursor.execute(sql_updata)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
            print("Error: renewdb.renew_count.updata error")

        db.close()
        return count
