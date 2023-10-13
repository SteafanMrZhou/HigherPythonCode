from concurrent.futures import ThreadPoolExecutor

mThreadPool = ThreadPoolExecutor(max_workers=2)

import time


def wait_on_b():
    time.sleep(5)
    print(b.result())
    return 5


def wait_on_a():
    time.sleep(5)
    print(a.result())
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)


def wait_on_future():
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(pow, 323, 1235)
        print(future.result())

    # f = executor.submit(pow, 5, 2)
    # print(f.result())


executor = ThreadPoolExecutor(max_workers=1)
executor.submit(wait_on_future)
