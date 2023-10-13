import threading
import queue

mQueue = queue.Queue()
mCondtion = threading.Condition()


def fairLockDemo():
    print("123")


for i in range(5):
    mQueue.put(threading.Thread(target=fairLockDemo))


def fairLock(thread_queues):
    mCondtion.acquire()
    try:
        for i in range(thread_queues.qsize()):
            currThread = thread_queues.get()
            if (currThread.is_alive()):
                break
            else:
                currThread.start()
                print(currThread.getName())
    finally:
        mCondtion.release()


# def fairLock(thread_queues):
#     mCondtion.acquire()
#     try:
#         if(thread_queues.qsize() == 0 || thread_queues.qsize() == 1):
#             print('没有足够数量的Python线程，调用Python公平锁失败')
#         for i in range(thread_queues.qsize()):
#             currThread = thread_queues.get()
#             if(currThread.is_alive()):
#                 break
#             else:
#                 currThread.start()
#                 print(currThread.getName())
#     finally:
#         mCondtion.release()



fairLock(mQueue)
