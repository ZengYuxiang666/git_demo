from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

day = int(input("今天是几号："))
hour = int(input("今天几点抢："))
minute = int(input("几分抢："))
starting_point = input("请输入出发点：")
distination = input("请输入目的地：")
data = input("请输入抢什么时候的票(2023-12-30)：")

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
time.sleep(30)

web.find_element_by_xpath('//*[@id="J-chepiao"]/a').click()
web.find_element_by_xpath('//*[@id="megamenu-3"]/div[1]/ul/li[1]/a').click()
time.sleep(2)
starttime = datetime.datetime(2023,12,day,hour,minute,0)

web.find_element_by_xpath('//*[@id="fromStationText"]').click()
web.find_element_by_xpath('//*[@id="fromStationText"]').send_keys(f'{starting_point}',Keys.ARROW_DOWN,Keys.ENTER)
web.find_element_by_xpath('//*[@id="toStationText"]').click()
web.find_element_by_xpath('//*[@id="toStationText"]').send_keys(f'{distination}',Keys.ENTER)
web.find_element_by_xpath('//*[@id="train_date"]').click()
web.find_element_by_xpath('//*[@id="train_date"]').clear()
web.find_element_by_xpath('//*[@id="train_date"]').send_keys(f'{data}',Keys.ENTER)
while datetime.datetime.now() < starttime :
    time.sleep(0.1)

while True :
    web.find_element_by_xpath('//*[@id="query_ticket"]').click()
    if iselementexist(web,'//*[@id="ticket_57000D62660C_09_13"]/td[13]/a') == True :
        web.find_element_by_xpath('//*[@id="ticket_57000D62660C_09_13"]/td[13]/a').click()
        break
    else:
        continue

while True :
    if iselementexist(web,'//*[@id="normalPassenger_0"]') == True :
        web.find_element_by_xpath('//*[@id="normalPassenger_0"]').click()
        web.find_element_by_xpath('//*[@id="submitOrder_id"]').click()
        break
    else:
        continue

while True :
    if iselementexist(web,'//*[@id="qr_submit_id"]') == True :
        try:
            web.find_element_by_xpath('//*[@id="qr_submit_id"]').click()
        except :
            continue

    else:
        continue


