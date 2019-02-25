#!/usr/bin/env python 
# encoding: utf-8 


"""
@python version: v3.5
@author: mzt
@software: PyCharm
@file: analysis_main.py
@time: 2019/2/25 8:33
"""
import pymysql
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import  LinearRegression

hot = np.array([0, 0, 0, 0, 0])
# 获取数据库信息
db = pymysql.connect("localhost", "root", "", "bigdata")
cursor = db.cursor()
sql = "SELECT * FROM `songs`"
#  WHERE `id`<100
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取记录
    results = cursor.fetchall()
    for li in results:
        sid = li[0]
        count = li[2]
        qianqian_hot = li[3]
        baidu_hot = li[4]
        kuwo_hot = li[7]
        if baidu_hot is not None:
            hot_data = np.array([sid, count, qianqian_hot, baidu_hot, kuwo_hot])
            hot = np.vstack((hot, hot_data))
        else:
            continue
except:
    print("Error: read_db.read_songs_name error")

db.close()
hot = np.delete(hot, 0, axis=0)
# print(hot)
# 整理成X，Y
X = np.delete(hot, [0, 1], axis=1)
Y = hot[:, 1]
print(X)
print(Y)
# x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=33)
# 带入函数

# # 梯度提升树
# rf0 = GradientBoostingClassifier(n_estimators=1000, max_depth=200, max_features=None, tol=1e-8)
# rf0.fit(x_train, y_train)
# predict = rf0.predict(x_test)
# print("匹配度：", rf0.score(x_test, y_test))

# 多元线性回归
regr=linear_model.LinearRegression()#创建模型
regr.fit(X,Y)
#y=b0+b1*x1+b2*x2
print("输出b1,b2和b0：")
print(regr.coef_)#b1,b2
print(regr.intercept_)#b0
predict = regr.predict(X)
y_test = Y
print("匹配度：", regr.score(X, Y))


# 输出图像
figure = plt.scatter(predict, y_test, marker='x', color='g', label='1', s=30)
plt.ylabel('True label')
plt.xlabel('Predicted label')
plt.show()
print(predict)
print(y_test)




