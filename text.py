
# def get_dec_lan(s):
#     return  0
#     loc = s.find('.')
#     if loc > 0:
#         return  len(s)-loc-1
#
# if __name__ == '__main__':
#     x = input('请输入第一个数字：')
#     y = input('请输入第二个数字：')
#     declan = get_dec_lan(x) + get_dec_lan(y)
#
#     z = str(int(x.replace('.','')) + int(y.replace('.','')))
#
#     if declan>0:
#         if len(z)<declan:
#             z = '0'*(declan-len(z)) + z
#         z = z[:-declan] + '.' + z[-declan:]
#
#     print('乘积是：',z)

import random
names = ['博士','学士','硕士','硕士','博士','学士','壮士','学士','圣斗士','生豆士']
d ={'学士':0,'硕士':1,'博士':2,'壮士':3,'生豆士':4,'圣斗士':5}
def dfd(i):
    for i in names:
       return d[i]
print(dfd('壮士'))


def ase(a,b):
    return a+b

a = ase(3,4)
print(a)

shit


