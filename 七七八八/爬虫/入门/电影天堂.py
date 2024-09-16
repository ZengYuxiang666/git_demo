import re

import requests
url = 'https://www.dytt.to/index.htm'
obj = re.compile(r"<a href='/html/gndy/jddy/(.*?).html'>(?P<zje>2023年.*?)</a><br/>",re.S)
resp = requests.get(url,verify=False)   # verify=False 去掉安全验证
resp.encoding = "utf-8"
result = obj.finditer(resp.text)
for x in result :
    print(x.group("zje"))