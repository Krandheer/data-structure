import threading as td
import time
from concurrent.futures import ThreadPoolExecutor


def fun(seconds):
    print(f"sleeping for {seconds}")
    time.sleep(seconds)


#
# n_start = time.perf_counter()
# fun(5)
# fun(3)
# fun(2)
# n_end = time.perf_counter()
# print(f"time in normal run: {n_end-n_start} seconds")


def main():
    tr_start = time.perf_counter()
    t1 = td.Thread(target=fun, args=[5])
    t2 = td.Thread(target=fun, args=[3])
    t3 = td.Thread(target=fun, args=[2])

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

    tr_end = time.perf_counter()
    print(f"time in thread run: {tr_end-tr_start} seconds")


def pool():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(fun, 4)
        # future2 = executor.submit(fun, 3)
        # future3 = executor.submit(fun, 2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        times = [3, 4, 2]
        results = executor.map(fun, times)
        for result in results:
            print(result)


pool()
