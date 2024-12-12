import asyncio
from asyncio import TimeoutError


async def one():
    await asyncio.sleep(3)
    print('one')


async def main():
    a = asyncio.create_task(one())
    try:
        await asyncio.wait_for(a, timeout=5)
    except TimeoutError:
        print('timeout')
    print(f"was that cancel task? {a.cancelled()}")


asyncio.run(main())
