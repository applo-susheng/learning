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
# chrome_options.add_argument('--headless') #headless模式下，浏览器窗口不可见，可提高效率

save_path = input("请输入保存地址：")
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': save_path  # 此处填写你希望文件保存的路径
}
chrome_options.add_argument('--kiosk-printing')  # 静默打印，无需用户点击打印页面的确定按钮
chrome_options.add_experimental_option('prefs', prefs)

#选择上传文件还是输入链接
def select():
    aorb = int(input('\n上传EXCEL文件----按1 \n输入名称及链接---按2  '))
    if aorb == 1:
        path = input('\n请输入上传文件的路径：')
        df = pd.read_excel(path,usecols=[0,1])#上传文件，默认读取第一二列
        df1 = df.dropna()
        Loadfile = dict(zip(df1[df1.columns.values[1]].tolist(),df1[df1.columns.values[0]].tolist()))
    elif aorb == 2 :
        Loadfile = LoadOneUrl()
    return Loadfile

#输入名称及链接
def LoadOneUrl():
    Loadfile = {}
    update_pdf = True
    while update_pdf:
        url = input('\n请输入链接：')
        title = input('请输入名称：')
        Loadfile[title] = url
        repeat = input('是否继续添加链接？（y/n) ')
        if repeat == 'y':
            continue
        elif repeat == 'n':
            update_pdf = False
            return Loadfile
        # else:
        #     return repeat

#打印,默认mode=1是自己设定的名称，mode=2是系统自带名称
def short_print(driver,title,url,mode=1):
    driver.set_page_load_timeout(15)#使用set_page_load_timeout时候，当页面未加载出任何东西的时候（往往是html源码未加载），因为超时而停止，会导致driver失效，后面的driver都不能操作，所以超时设置应该至少保证页面内容加载出来一部分，设置超时不宜过短
    driver.set_script_timeout(15)#设置页面异步js执行超时
    #driver.maximize_window()
    try:
        driver.get(url)
        #driver.maximize_window()
        if mode == 1:
            driver.execute_script('document.title="{}";window.print()'.format(title))
        elif mode == 2:
            driver.execute_script('window.print()')
        # 'document.title="{}";window.print();'.format(url) #利用js修改网页的title，该title最终就是PDF文件名，利用js的window.print可以快速调出浏览器打印窗口，避免使用热键ctrl+P
    except:
        driver.execute_script('window.close()')
        print('该网页未截屏成功:', url)
        with open('未截屏成功的网页.text','a') as f:
            f.write(url + ":" + str(title) + "\n")

def run():
    while True:
        Custom_name = int(input('\n选择自定义名称----按1 \n选择系统默认名称--按2 \n退出-------------按3  '))
        if Custom_name == 3:
            break
        Loadfile = select()
        driver = webdriver.Chrome(options=chrome_options)
        for title, url in Loadfile.items():
            short_print(driver,title,url,Custom_name)
        driver.close()

if __name__ == '__main__':
    run()
