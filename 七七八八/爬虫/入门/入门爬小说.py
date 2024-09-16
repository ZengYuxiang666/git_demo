import re
import requests
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
num = 68208370
obj = re.compile(r"<p>(?P<zje>.*?)</p>",re.S)   #re.S能让“.”匹配所有字符    ?P<...> 给分组起名
headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }


def func(num):
    url = f'https://read.zongheng.com/chapter/1215341/{str(num)}.html'
    resp = requests.get(url=url, headers=headers)
    if '错误页' not in resp.text:
        result = obj.finditer(resp.text)
        for it in result:
            print(it.group("zje"))
        print("\n")
        print(
            "-------------------------------------------------------------------------------------------------------------------------------------")
        print("\n")


while True :
    with ThreadPoolExecutor(100) as executor:
        for _ in range(10):  # 提交10个任务到线程池，你可以根据需要调整这个数字
            executor.submit(func, num)
            num += 1
