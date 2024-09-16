from selenium.webdriver import Edge
from selenium.webdriver.common.keys import Keys
# 1.创建浏览器对象
web = Edge()
# 2.打开一个网址
web.get("http://lagou.com")
# 找到某个元素，点击它
el = web.find_element_by_xpath('/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/ul/li[1]/a')
el.click()

# 找到输入框，输入python  输入回车/点击搜索按钮
web.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/div[1]/form/input[1]').send_keys("python",Keys.ENTER)

web.find_element_by_xpath('//*[@id="openWinPostion"]').click()

# 在selenium的眼中，新窗口默认是不切换过来的
web.switch_to.window(web.window_handles[-1])
job_detail = web.find_element_by_xpath('//*[@id="job_detail"]/dd[2]/div/p').text
print(job_detail)

# 关掉子窗口
web.close()
# 转到原来的窗口
web.switch_to.window(web.window_handles[0])

# 如果页面中遇到了iframe如何处理
# web.get("pass")
# 处理iframe的话，必须先拿到iframe，然后视角到iframe，然后才可以哪数据
# iframe = web.find_element_by_xpath('pass')
# web.switch_to.frame(iframe)
# web.switch_to.default_content()  #切换到原页面
# tx = web.find_element_by_xpath('pass').text