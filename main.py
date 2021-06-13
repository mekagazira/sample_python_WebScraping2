from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

import pandas as pd

# 参照先ページ
url = "https://info.finance.yahoo.co.jp/ranking/?kd=1&mk=3&tm=d&vl=a"

# ブラウザ起動・ページ表示
browser = webdriver.Chrome("chromedriver.exe")
browser.get(url)

# 一時停止
sleep(1)

elements_table = browser.find_element_by_class_name("rankingTable")
trs = elements_table.find_elements(By.TAG_NAME, "tr")

keys = []

for i in range(1, len(trs)):
    tds = trs[i].find_elements(By.TAG_NAME, "td")
    line = []
    for tmp in tds:
            line.append(tmp.text)
    keys.append(line)

print(keys)

# 一時停止
sleep(1)

# ブラウザ停止
browser.quit()