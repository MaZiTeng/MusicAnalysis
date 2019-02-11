# coding :utf8

# -*- coding: UTF-8 -*-
import urllib
import urllib.parse
from .database import read_db


class UrlManager(object):
    def __init__(self):
        self.read_db = read_db.ReadDatabase()

    def get_name(self, rid):
        # print("从数据库拿取第", rid, "首音乐的名字")
        tail = self.read_db.read_songs_name(rid)
        # print("数据库", tail)
        return tail
