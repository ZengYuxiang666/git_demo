import time

from selenium.webdriver import Edge
from chaojiying import Chaojiying_Client
web = Edge()
web.get("https://www.chaojiying.com/user/login/")

# 处理验证码
img = web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png

chaojiying = Chaojiying_Client('zengyuxiang', '1301556431zyx', '955555')
dic = chaojiying.PostPic(img,1902)
verify_code = dic['pic_str']

# 向页面中填入用户名，密码，验证码
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys("zengyuxiang")
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('1301556431zyx')
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)

#点击登录
web.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()