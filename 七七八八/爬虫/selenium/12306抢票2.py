from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
day = int(input("今天是几号："))
hour = int(input("今天几点抢："))
minute = int(input("几分抢："))

# 用来判断一个元素存不存在
def iselementexist(web,xpath):
    try:
        element = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return True
    except:
        return False


option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Edge(options=option)
web.get( 'https://kyfw.12306.cn/otn/resources/login.html')

#扫码登录
time.sleep(60)
starttime = datetime.datetime(2023,12,day,hour,minute,0)

while datetime.datetime.now() < starttime :
    time.sleep(0.01)

while True :
    web.find_element_by_xpath('//*[@id="query_ticket"]').click()
    if iselementexist(web,'//*[@id="ticket_55000K13730A_08_10"]/td[13]/a') == True :
        web.find_element_by_xpath('//*[@id="ticket_55000K13730A_08_10"]/td[13]/a').click()
        break
    else:
        continue
time.sleep(0.5)
while True :
    if iselementexist(web,'//*[@id="normalPassenger_0"]') == True :
        web.find_element_by_xpath('//*[@id="normalPassenger_0"]').click()
        web.find_element_by_xpath('//*[@id="submitOrder_id"]').click()
        select = Select(web.find_element_by_xpath('//*[@id="seatType_1"]'))
        time.sleep(0.5)
        select.select_by_visible_text('硬座（¥72.0元）')
        break
    else:
        continue
time.sleep(0.5)
while True :
    if iselementexist(web,'//*[@id="qr_submit_id"]') == True :
        try:
            web.find_element_by_xpath('//*[@id="qr_submit_id"]').click()
        except :
            continue

    else:
        continue


