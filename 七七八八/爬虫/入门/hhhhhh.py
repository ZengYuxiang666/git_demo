import re
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor

obj = re.compile(r"<p>(?P<zje>.*?)</p>", re.S)  # re.S能让“.”匹配所有字符    ?P<...> 给分组起名
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
}


async def func(num):
    url = f'https://read.zongheng.com/chapter/1215341/{str(num)}.html'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if '错误页' not in await resp.text():
                result = obj.finditer(await resp.text())
                for it in result:
                    print(it.group("zje"))
                print("\n")
                print(
                    "-------------------------------------------------------------------------------------------------------------------------------------")
                print("\n")
            # 在函数的最后，我们返回result列表
            return result  # 添加返回结果，以便外部可以获取到结果

async def main():
    num = 68208370
    tasks = []
    for _ in range(10):  # 提交10个任务到线程池，你可以根据需要调整这个数字
        num += 1
        tasks.append(func(num))  # 使用asyncio.run来启动协程
    await asyncio.gather(*tasks)  # 使用gather来等待所有协程完成，代替之前的asyncio.wait(tasks) # 使用*运算符解包tasks列表


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # 获取事件循环
    loop.run_until_complete(main())  # 在事件循环中运行main协程
    loop.close()  # 关闭事件循环
