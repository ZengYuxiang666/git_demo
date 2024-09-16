import requests
from bs4 import BeautifulSoup
url = 'http://www.xinfadi.com.cn/getCat.html'
resp = requests.post(url)
page = BeautifulSoup(resp.text,'html.parser')    #指定html解析器,创建bs对象

# 从bs对象中获取数据
# find(标签，属性=值)
# findall(标签，属性=值)
# 在bs对象中，  .text 表示被标签标记的数据