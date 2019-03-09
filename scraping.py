import time
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# まとめ処理
# pip install忘れずに
wb = xlrd.open_workbook('example.xlsx')

# シート数分やりたいところ
def captureSponseredSearch():
    for i in wb.sheet_names():
        # シート取得
        sheet = wb.sheet_by_index(i)
        # 行数に応じたデータ取得
        accountId = sheet.cell(0, 0)
        accountPs = sheet.cell(1, 0)
        accuontList = sheet.col_values(2)

        driver = start_chrome()
        login = loginSs(accountId, accountPs)

        fot pageNum in accountList:
             url = 'https://promotionalads.business.yahoo.co.jp/biz/ss/accounts/' + pageNum + '/reports/#/detailedstatements'
             # スクショとってくる
             screenShotSs(url, pageNum)

        driver.quit()
