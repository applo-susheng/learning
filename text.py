import os, json, time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

#save_path = input("请输入保存地址：")
prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': 'F:\下载文件\截屏' # 此处填写你希望文件保存的路径
}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--enable-print-browser')  # 启用PrintBrowser模式，其中所有内容都呈现为打印
chrome_options.add_argument('--kiosk-printing')  # 静默打印，无需用户点击打印页面的确定按钮
chrome_options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(options=chrome_options)
driver.set_page_load_timeout(10)
driver.set_script_timeout(10)
try:
    driver.get(r'https://blog.csdn.net/ginynu/article/details/63697559')
except:
    driver.execute_script('window.stop')