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

## Differencere between parallelism and concurrency
#Concurrency and parallelism are names for two different mechanisms for juggling
# tasks in programming Concurrency involves allowing multiple jobs to take turns
# accessing the same shared resources, like disk, network, or a single CPU core.
# Parallelism is about allowing several tasks to run side by side on independently
#  partitioned resources, like multiple CPU cores.

#Concurrency and parallelism have different aims. The goal of concurrency is to 
#prevent tasks from blocking each other by switching among them when one is forced
#to wait on an external resource. A common example is completing multiple network requests.
#The crude way to do it is to launch one request, wait for it to finish, launch another,
#and so on. The concurrent way to do it is to launch all requests at once, 
#then switch among them as they get responses back. Through concurrency, 
#we can aggregate all the time spent waiting for responses.

#Parallelism, by contrast, is about maximizing the use of hardware resources. 
#If you have eight CPU cores, you don’t want to max out only one while the other seven lie idle.
# Rather, you want to launch processes or threads that make use of all those cores, if possible.

..