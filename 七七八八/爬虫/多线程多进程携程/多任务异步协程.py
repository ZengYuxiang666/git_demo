import asyncio
import time

async def func1() :
    print('hh1')
    await asyncio.sleep(2)
    print('hh2')

async def func2():
    print('hh3')
    await asyncio.sleep(3)
    print('hh4')

async def func3() :
    print('hh5')
    await asyncio.sleep(4)
    print('hh5')

async def main() :
    # 第一种写法
    #f1 = func1()   创建协程对象
    #await fi    #一般await挂起操作放在协程对象前面
    #第二种写法（推荐）
    tasks = [
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3()),
        ]
    await asyncio.wait(tasks)

if __name__ == '__main__' :
    asyncio.run(main())