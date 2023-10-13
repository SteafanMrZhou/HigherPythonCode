import asyncio
import time


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


asyncio.run(main())


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main2():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main2())


async def main3():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main3())
