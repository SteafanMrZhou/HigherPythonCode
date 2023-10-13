import time
import datetime
from concurrent.futures import ThreadPoolExecutor


def threadAsyncDemo():
    max_value = 4
    thread_pool = ThreadPoolExecutor(max_workers=max_value)
    print('线程池最大数量：{}'.format(max_value))

    for i in [3, 2, 6, 1, 7]:
        # 提交具体任务
        thread_pool.submit(i)
    print('{} --> 我是主线程'.format(time.ctime()))


def threadAsyncDemotest(sleep_time):
    print('{} --> start sleep_time ({})'.format(datetime.datetime.now(), sleep_time))
    time.sleep(sleep_time)
    print('{} --> sleep_time ({}) finish'.format(datetime.datetime.now(), sleep_time))
