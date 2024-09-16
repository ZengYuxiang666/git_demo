from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 用来判断一个元素存不存在
def iselementexist(web):
    try:
        element = WebDriverWait(web, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ticket_57000D62660C_09_13"]/td[13]/a')))
        return True
    except:
        return False


option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Edge(options=option)
web.get( 'https://kyfw.12306.cn/otn/resources/login.html')
web.find_element_by_xpath('//*[@id="J-userName"]').send_keys('18397881293')
web.find_element_by_xpath('//*[@id="J-password"]').send_keys('1301556431zyx')
web.find_element_by_xpath('//*[@id="J-login"]').click()
time.sleep(2)
web.find_element_by_xpath('//*[@id="id_card"]').send_keys('3059')
web.find_element_by_xpath('//*[@id="verification_code"]').click()
time.sleep(20)
web.find_element_by_xpath('//*[@id="sureClick"]').click()
time.sleep(3)
web.find_element_by_xpath('//*[@id="J-chepiao"]/a').click()
web.find_element_by_xpath('//*[@id="megamenu-3"]/div[1]/ul/li[1]/a').click()
time.sleep(2)
starttime = datetime.datetime(2023,12,11,9,18,0)

web.find_element_by_xpath('//*[@id="fromStationText"]').click()
web.find_element_by_xpath('//*[@id="fromStationText"]').send_keys('景德镇',Keys.ARROW_DOWN,Keys.ENTER)
web.find_element_by_xpath('//*[@id="toStationText"]').click()
web.find_element_by_xpath('//*[@id="toStationText"]').send_keys('鹰潭',Keys.ENTER)
web.find_element_by_xpath('//*[@id="train_date"]').click()
web.find_element_by_xpath('//*[@id="train_date"]').clear()
web.find_element_by_xpath('//*[@id="train_date"]').send_keys('2023-12-17',Keys.ENTER)
while datetime.datetime.now() < starttime :
    print("时间未到")
    time.sleep(0.1)
while True :
    web.find_element_by_xpath('//*[@id="query_ticket"]').click()
    if iselementexist(web) == True :
        break
    else:
        continue
web.find_element_by_xpath('//*[@id="ticket_57000D62660C_09_13"]/td[13]/a').click()
time.sleep(1)
web.find_element_by_xpath('//*[@id="normalPassenger_0"]').click()
web.find_element_by_xpath('//*[@id="submitOrder_id"]').click()
# //*[@id="ticket_57000D62660C_09_13"]/td[13]/a
time.sleep(3)
web.find_element_by_xpath('//*[@id="qr_submit_id"]').click()

