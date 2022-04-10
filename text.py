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

from random import randint
import pygal
class de():
    def __init__(self,num=6):
        self.num=num
    def roll(self):
        return randint(1,self.num)

de = de()
results =[]
for i in range(1000):
    result = de.roll()
    results.append(result)

ss = []
for i in range(1,de.num+1):
    ss1 = results.count(i)
    ss.append(ss1)
