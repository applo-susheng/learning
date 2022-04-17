# import matplotlib.pyplot as plt
# rt = list(range(10001))
# fd = [x**2 for x in rt]
# plt.scatter(rt,fd,c=rt,cmap=plt.cm.Blues,s=50)#生产点图
# plt.title('TEST',fontsize=24)
# plt.xlabel('value',fontsize=14)
# plt.ylabel('key',fontsize=14)
# plt.tick_params(axis='both',which='major',labelsize=10)
# plt.axis([0,1700,0,3000000])#坐标
# plt.show()


#随机漫步画图
# from random import choice
# import matplotlib.pyplot as plt
# class RdandomWalk():
#     def __init__(self,num_points=5000):
#         self.num_points = num_points
#         self.xvalue=[0]
#         self.yvalue=[0]
#
#     def fill_walk(self):
#         while len(self.xvalue) < self.num_points:
#             xdire = choice([1,-1])
#             xdist =choice([0,1,2,3,4])
#             xstep = xdire*xdist
#
#             ydire = choice([1,-1])
#             ydist =choice([0,1,2,3,4])
#             ystep = ydire*ydist
#
#             if xstep == 0 and ystep == 0:
#                 continue
#
#             nextx = self.xvalue[-1] + xstep
#             nexty = self.yvalue[-1] + ystep
#
#             self.xvalue.append(nextx)
#             self.yvalue.append(nexty)
#
# while True:
#     se = RdandomWalk()
#     se.fill_walk()
#     p_num = list(range(se.num_points))
#     plt.figure(dpi=100,figsize=(10,20))
#     plt.scatter(se.xvalue,se.yvalue,c=p_num,cmap=plt.cm.Blues,s=15)#scatter可以多次调用，且生成到同一图表上
#     plt.scatter(0,0,c='green',s=100)
#     plt.scatter(se.xvalue[-1],se.yvalue[-1],c='green',s=100)
#     plt.axes().get_xaxis().set_visible(False)#隐藏坐标轴
#     plt.axes().get_yaxis().set_visible(False)#隐藏坐标轴
#     plt.show()
#
#     keepdoing = input('y/n')
#     if keepdoing == 'n':
#         break

#利用pygal制图
# from random import randint
# import pygal
# class de():
#     def __init__(self,num=6):
#         self.num=num
#     def roll(self):
#         return randint(1,self.num)
#
# de = de()
# results =[]
# for i in range(1000):
#     result = de.roll()
#     results.append(result)
#
# ss = []
# for i in range(1,de.num+1):
#     ss1 = results.count(i)
#     ss.append(ss1)
#
# hist = pygal.Bar()
# hist.title = 'result of rolling 1000 times'
# hist.x_labels = ['1','2','3','4','5','6']
# hist.x_title = 'result'
# hist.y_title = 'ss of result'
# hist.add('D6',ss)
# hist.render_to_file('de.svg')

#温度制表
# import time
# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
# start = time.clock()
# path = 'D:\下载专区\python编程入门到实践\pcc-master\chapter_16\sitka_weather_2014.csv'
# with open(path) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#     dates,highs,lows = [],[],[]
#     for i in reader:
#         cdate = datetime.strptime(i[0],"%Y-%m-%d")
#         dates.append(cdate)
#         highs.append(int(i[1]))
#         lows.append(int(i[3]))
#     fig = plt.figure(dpi=128,figsize=(10,6))
#     plt.plot(dates,highs,c='red',alpha=0.5)
#     plt.plot(dates,lows,c='blue',alpha=0.5)
#     plt.fill_between(dates,highs,lows,facecolor='green',alpha=0.5)
#     plt.title('Daiy high temperatures,2014')
#     plt.xlabel("",fontsize=16)
#     plt.ylabel('temp',fontsize=16)
#     plt.show()
# end = time.clock()
# print(end-start)


# import requests
# import json
# json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = requests.get(json_url)
# btcdata = response.json()
# for row in btcdata:
#     date = row['date']
#     month = row['month']
#     print(row)


from fuzzywuzzy import process
import pandas as pd

#原始模板
# def fuzzy_merge(df1,df2,key1,key2,threshold=90,limit=3):
#         df1['企业相似度百分比'] = df1[key1].apply(lambda x: process.extract(x, df2[key2].tolist(),limit=limit))
#         df1['匹配度最高企业'] = df1['企业相似度百分比'].apply(lambda x : [i[0] for i in x if i[1] >= threshold][0] if len([i[0] for i in x if i[1] >= threshold]) > 0 else "")
#     return df1

#添加了新的属性，多两个条件进行匹配
# def IfFuzzyMerge(df1,df2,first_key1,first_key2,second_key1,second_key2,threshold=90,limit=3):
#     df = pd.DataFrame()
#     values = df2[second_key2].unique() #返回不重复值
#     for value in values:
#         df1['企业相似度百分比'] = df1[df1[second_key1]==value][first_key1].apply(lambda x: process.extract(x, df2[df2[second_key2]==value][first_key2].tolist(),limit=limit))
#         df = pd.concat([df,df1], ignore_index=True)   #纵轴拼接
#         df = df[df['企业相似度百分比'].notnull()]        #去掉空值
#         df['匹配度最高企业'] = df['企业相似度百分比'].apply(lambda x : [i[0] for i in x if i[1] >= threshold][0] if len([i[0] for i in x if i[1] >= threshold]) > 0 else "")
#     return df
#
# df1 = pd.read_excel(r'F:\新建文件夹\2021年汇总.xlsx')
# df2 = pd.read_excel(r'F:\新建文件夹\2021年汇总.xlsx',sheet_name=1)
#
# match_data = IfFuzzyMerge(df1,df2,'企业名称','企业名称','省','省')
# data = pd.merge(match_data,df2,how='left',left_on=['匹配度最高企业'],right_on=['企业名称'])
# with pd.ExcelWriter(r'F:\新建文件夹\待匹配名称的监测企业(保存）.xlsx',   mode ='a', engine='openpyxl',if_sheet_exists='new') as writer:
#     match_data.to_excel(writer,sheet_name='test1')

#error test
# import traceback
# try:
#     raise Exception('this is an error')
# except:
#     errofile = open('error.txt','w')
#     errofile.write(traceback.format_exc())
#     errofile.close()
#     print('nothing,just test')

import os

for path,noting,name in os.walk('D:\下载专区\EXCEL模板 - 副本'):
    for i in name:
        newname = path
        print(path)

