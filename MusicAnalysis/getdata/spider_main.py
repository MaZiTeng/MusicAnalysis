# coding :utf8

from MusicAnalysis.getdata.action import url_manager, hot_do
from MusicAnalysis.getdata.action.database import check_in, create, renewdb
from MusicAnalysis.getdata.action.module import module


class SpiderMain(object):

    def __init__(self):
        self.module = module.Module()
        self.urls = url_manager.UrlManager()
        self.hot = hot_do.HotDo()
        self.check = check_in.CheckDatabase()
        self.create = create.CreateRecords()
        self.renew = renewdb.RenewDatabase()

    def craw(self):

        for i in range(17658, 20000):
            # 从数据库中获取第i歌曲名
            music_name = self.urls.get_name(i)
            print("\n正在处理第 %s 条数据，%s" % (i, music_name))
            if music_name is 0:
                continue
            # 处理这个名字
            music_name = self.module.wash_data(music_name)
            # 检查这条记录是否存在于数据库
            ex, wid = self.check.check_in(music_name)
            if ex is 0:
                # 判断它是否是歌曲
                judge, hot_baidu = self.hot.judge_music(music_name)
                if judge is 0:
                    continue
                # 在新数据库中创建这条记录
                wid = self.create.create_records(music_name)
                # 获取热度
                hot1, hot2, hot3, hot4 = self.hot.hot_do(music_name, wid, hot_baidu)
                print("插入数据：", wid, music_name, hot1, hot_baidu, hot2, hot3, hot4)

            else:
                # 更新数据库bigdata
                count = self.renew.renew_count(wid)
                print("更新数据：", wid, music_name, count)


if __name__ == "__main__":

    obj_spider = SpiderMain()
    obj_spider.craw()
