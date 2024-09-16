import requests
import re
url = 'https://jdxy.jci.edu.cn/tzgg.htm'
resp = requests.get(url)
resp.encoding = 'utf-8'
obj = re.compile(r"<a href=.*?.info.*?>(?P<zje>.*?)</a>",re.S)   #re.S能让“.”匹配所有字符    ?P<...> 给分组起名
result = obj.finditer(resp.text)
for x in result :
    print(x.group("zje"))

