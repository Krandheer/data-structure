import asyncio
from datetime import datetime
import time


def anything(j):
    """test functions
    plain old blocking function"""
    print(j, datetime.now())
    time.sleep(j)


async def async_anything(j):
    """async functions is coroutine function
    asynchronous function"""
    print(j, datetime.now())
    await asyncio.sleep(j)
    print(f"task {j} done")


if __name__ == "__main__":
    event_lopp = asyncio.get_event_loop()
    task = [event_lopp.create_task(async_anything(i)) for i in range(1, 4)]
    # below code proves that it simply works like javascript, basically waiting
    # in loop till main thread is free
    # for i in range(4):
    #     time.sleep(1)
    try:
        event_lopp.run_until_complete(asyncio.wait(task))
    finally:
        event_lopp.close()
