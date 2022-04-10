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
from random import randint
import pygal
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
# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
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

import requests
import json
json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = requests.get(json_url)
btcdata = response.json()
for row in btcdata:
    date = row['date']
    month = row['month']
    print(row)
