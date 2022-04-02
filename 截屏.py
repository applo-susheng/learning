# -*-coding=UTF-8-*-
# @Time : 2022/3/31 15:38
# @Author : Su
# @File : 截屏.py
# @Software :PyCharm

import os, json, time
from selenium import webdriver
import pandas as pd

settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": ""
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    # "customMargins": {},
    # "marginsType": 2,
    # "scaling": 100,
    # "scalingType": 3,
    # "scalingTypePdf": 3,
    "isLandscapeEnabled": True,  # landscape横向，portrait 纵向，若不设置该参数，默认纵向
    "isHeaderFooterEnabled": True,  # 是否打印页眉页脚
    "isCssBackgroundEnabled": True,  # 是否打印背景
    "mediaSize": {
        "height_microns": 297000,
        "name": "ISO_A4",
        "width_microns": 210000,
        "custom_display_name": "A4 210 x 297 mm"  # 设定为A4尺寸
    },
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--enable-print-browser')  # 启用PrintBrowser模式，其中所有内容都呈现为打印
# chrome_options.add_argument('headless') #headless模式下，浏览器窗口不可见，可提高效率

prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': r'Z:\重点排污单位及企业名录\企业信息依法披露名单\2022源文件'  # 此处填写你希望文件保存的路径
}
chrome_options.add_argument('--kiosk-printing')  # 静默打印，无需用户点击打印页面的确定按钮
chrome_options.add_experimental_option('prefs', prefs)


def short_print(title, url):
    driver.get(url)
    driver.maximize_window()
    driver.execute_script('document.title="{}";window.print();'.format(title))
    # 'document.title="{}";window.print();'.format(url) #利用js修改网页的title，该title最终就是PDF文件名，利用js的window.print可以快速调出浏览器打印窗口，避免使用热键ctrl+P


# 单个文件
# url1 = {'123':'https://www.xinji.gov.cn/html/gggs/150563.html',
#     '234':'http://sthjj.tangshan.gov.cn/sthjj/tzgg/20220316/1412401.html'}

# 多个文件读取
path = input('请输入链接：')
df = pd.read_excel(path)

url = []
title = []
for i in df[df.columns.values[0]]:
    url.append(i)
for j in df[df.columns.values[1]]:
    title.append(j)
Loadpdf = dict(zip(title, url))

driver = webdriver.Chrome(options=chrome_options)

# 单个文件用url1,输入文件用Loadpdf
for title, url in Loadpdf.items():
    short_print(title, url)
    time.sleep(5)

driver.close()
