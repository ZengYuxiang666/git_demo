import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Edge
from selenium.webdriver.support.select import Select

# 准备好参数配置
opt = Options()
opt.add_argument("--headless")
opt.add_argument("--disbale-gpu")


web = Edge(options=opt)
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
# 定位下拉列表
sel_el= web.find_element_by_xpath('//*[@id="OptionDate"]')
# 对下拉列表进行包装，包装成下拉菜单
sel = Select(sel_el)
# 让浏览器进行调整选项
for i in range(len(sel.options)):
    sel.select_by_index(i) #按照索引进行切换
    table = web.find_element_by_xpath('//*[@id="TableList"]/table/tbody').text
    print(table)
    print('=========================================================================================================')