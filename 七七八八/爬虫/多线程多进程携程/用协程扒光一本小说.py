# https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224356374661%22}
# https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224356374661%22,%22cid%22:%224356374661|1571468531%22,%22need_bookinfo%22:1}
import requests
import asyncio
import aiohttp
import json
import aiofiles
async def aiodownload(cid,b_id,title) :
    data = {
        "book_id" : b_id,
        "cid" : f"{b_id}|{cid}",
        "need_bookinfo" : 1
    }
    data = json.dumps(data)
    url = f"https://dushu.baidu.com/api/pc/getChapterContent?data={data}"
    async with aiohttp.ClientSession() as session :
        async with session.get(url) as resp :
            dic = await resp.json()
            async with aiofiles.open(title,mode='w',encoding='utf-8') as f :
                await f.write(dic['data']['novel']['content'])



async def getCatalog(url) :
    resp = requests.get(url)
    dic = resp.json()
    tasks = []
    for x in dic['data']['novel']['items'] :
        title = x['title']
        cid = x['cid']
        #准备异步任务
        tasks.append(aiodownload(cid,b_id,title))
    await asyncio.wait(tasks)

if __name__ == '__main__' :
    b_id = '4356374661'
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224356374661%22}'
    asyncio.run(getCatalog(url))