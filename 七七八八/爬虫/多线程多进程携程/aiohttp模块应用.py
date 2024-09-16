import asyncio
import aiohttp

urls = [
    "https://i1.huishahe.com/uploads/allimg/202205/9999/a703018f22.jpg",
    "https://i1.huishahe.com/uploads/tu/202205/42/0883978edc.jpg",
    "https://i1.huishahe.com/uploads/tu/202205/39/18ef88e931.jpg"
]

async def aiodownload(url):
    name = url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session :
        async with session.get(url) as resp :
            with open(name,mode="wb") as f :
                f.write(await resp.content.read())  #读取内容是异步的，需要await挂起
    print("over!!!")

    # s = aiohttp.ClientSession()  与 requests等价


async def main():
    tasks = []
    for url in urls :
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)

if __name__ == '__main__' :
    asyncio.run(main())
