from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
option = Options()
option.add_argument('--disable-blink-features=AutomationControlled')
web = Edge(options=option)
web.get( 'https://www.damai.cn/')
time.sleep(5)
# 移动滑块
btn = web.find_element_by_xpath('//*[@id="nc_1_n1z"]')
ActionChains(web).drag_and_drop_by_offset(btn,300,0).perform()
# 登录
web.find_element_by_xpath('/html/body/div[2]/div/div[3]/div[1]/div[1]/span').click()
time.sleep(5)
web.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('18397881293')
web.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('1301556431zyxzyx')
time.sleep(5)
web.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
web.find_element_by_xpath('//*[@id="J_GetCode"]').click()
time.sleep(20)
web.find_element_by_xpath('//*[@id="btn-submit"]').click()


web.find_element_by_xpath('/html/body/div[4]/a[1]').click()
# 切换到新页面
web.switch_to.window(web.window_handles[-1])
web.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div[1]').click()
web.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div/input').send_keys('曾雨祥')
web.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[3]/div/div/input').send_keys('430302200505133059')
web.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]/div/div[7]/div[1]').click()
web.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[3]/div[1]/div/div[1]/a/img').click()
web.find_element_by_xpath('//*[@id="dmViewerBlock_DmViewerBlock"]/div[2]/div/div').click()
web.find_element_by_xpath('//*[@id="dmContactBlock_DmContactBlock"]/div[2]/div/div/input').send_keys('曾雨祥')
web.find_element_by_xpath('//*[@id="dmOrderSubmitBlock_DmOrderSubmitBlock"]/div[2]/div/div[2]/div[2]/div[2]/span').click()


