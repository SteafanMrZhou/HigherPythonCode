from queue import Queue
from threading import Thread


def producer(pthreadProQueue):
    # 生成业务所需数据data
    pthreadProQueue.put()


def consumer(pthreadConQueue):
    # 获取业务所需数据data
    data = pthreadConQueue.get()
    # 根据实际业务情况继续处理数据data


q = Queue()
conThread = Thread(target=consumer, args=(q,))
proThread = Thread(target=producer, args=(q,))
proThread.start()
conThread.start()
