import re
import asyncio
import aiohttp
from bs4 import BeautifulSoup

obj = re.compile(r"<p>(?P<zje>.*?)</p>", re.S)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}


async def func(num):
    url = f'https://read.zongheng.com/chapter/1215341/{str(num)}.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            if '错误页' not in await resp.text():
                soup = BeautifulSoup(await resp.text(), 'html.parser')
                result = obj.finditer(str(soup))
                for it in result:
                    print(it.group("zje"))
                print("\n")
                print(
                    "-----------------------------------------------------------------------------------------------------------------------------------------")
                print("\n")


async def main():
    num = 68208370
    tasks = []
    for _ in range(10):  # Submit 10 tasks to the task list
        num += 1
        tasks.append(func(num))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())