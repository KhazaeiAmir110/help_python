import asyncio


async def one(name):
    await asyncio.sleep(10)
    print(f"Hellow {name}")


async def main():
    a1 = asyncio.create_task(one("a"))
    a2 = asyncio.create_task(one("b"))

    await a1, a2


asyncio.run(main())
