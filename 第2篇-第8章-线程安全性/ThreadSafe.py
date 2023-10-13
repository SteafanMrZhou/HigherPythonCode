import threading
import queue

mLock = threading.Lock()


def threadPrintDemo():
    print("Python ThreadSafe Printing")


mThreads = []
for i in range(10):
    mThreads.append(threading.Thread(target=threadPrintDemo))

for i in range(len(mThreads)):
    mLock.acquire()
    mThreads[i].start()
    mLock.release()

mQueue = queue.Queue()
mCondtion = threading.Condition()


def fairLockDemo():
    print("Python ThreadSafe Printing ")


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
    finally:
        mCondtion.release()


fairLock(mQueue)
