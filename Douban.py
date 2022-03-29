# -*-coding=UTF-8-*-
# @Time : 2022/3/21 13:35
# @Author : Su
# @File : Douban.py
# @Software :PyCharm


from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseurl = 'https://book.douban.com/tag/{}?start=0&type=S'.format()
    datalist = getData(baseurl)

#浏览一个网页
def askURL(url):
    header={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
    }
    request = urllib.request.Request(url=url, headers=header)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#获取所有网页的数据
def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)
    return datalist

def saveData():
    pass


if __name__== '__main__':
     main()


