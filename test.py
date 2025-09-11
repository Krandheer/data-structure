import asyncio
from concurrent.futures import ProcessPoolExecutor
from re import A
import time
from unittest import result


def fetch_data(param):
    print(f"do something with {param}", flush=True)
    time.sleep(param)
    print(f"done with {param}", flush=True)
    return f"result for {param}"


async def main():
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))
    result1 = await task1
    print("thread one fully complete")
    result2 = await task2
    print("thread two fully complete")

    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:
        task1 = loop.run_in_executor(executor, fetch_data, 1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)
        result1 = await task1
        print("thread one fully complete")
        result2 = await task2
        print("thread two fully complete")
    return result1, result2


if __name__ == "__main__":
    t1 = time.perf_counter()
    results = asyncio.run(main())
    print(results)
    t2 = time.perf_counter()
    print(f"Program complete in {t2 - t1:.2f} seconds")
