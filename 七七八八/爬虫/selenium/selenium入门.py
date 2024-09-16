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

div_list = web.find_elements_by_xpath('//*[@id="jobList"]/div[1]/div')

for div in div_list :
    job_name = div.find_element_by_tag_name("a").text
    job_price = div.find_element_by_xpath('./div[1]/div[1]/div[2]/span').text
    print(job_name,job_price)