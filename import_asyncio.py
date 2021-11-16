import asyncio,time

async def anotherfunc1():
    await asyncio.sleep(1)
    print("Another func1", time.strftime('%X'))

async def anotherfunc2():
    await asyncio.sleep(2)
    print("Another func2", time.strftime('%X'))

async def func():
    print("Start at", time.strftime('%X'))
    task_1 = asyncio.create_task(anotherfunc1())
    task_2 = asyncio.create_task(anotherfunc2())

    await task_1
    await task_2

asyncio.run(func())