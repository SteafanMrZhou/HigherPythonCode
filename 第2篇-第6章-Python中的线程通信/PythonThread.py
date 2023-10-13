import queue
import threading
from threading import Thread


def threadOrderTest():
    print(123)
    print(threading.current_thread())


testThreadA = Thread(target=threadOrderTest)
testThreadB = Thread(target=threadOrderTest)
testThreadC = Thread(target=threadOrderTest)
testThreadD = Thread(target=threadOrderTest)
testThreadE = Thread(target=threadOrderTest)
testThreadF = Thread(target=threadOrderTest)
testThreadG = Thread(target=threadOrderTest)

testThreadA.start()
testThreadB.start()
testThreadC.start()
testThreadD.start()
testThreadE.start()
testThreadF.start()
testThreadG.start()


def orderThreadByLock():
    for i in range(7):
        # mThreadList.append(Thread(target=printTemp))
        mt = Thread(target=printTemp)
        mt.start()
        mt.join()


def printTemp():
    print(123)
    print(threading.current_thread())


orderThreadByLock()


def orderThreadPrintA():
    print("A")


def orderThreadPrintB():
    print("B")


def orderThreadPrintC():
    print("C")


mPTQueue = queue.PriorityQueue()
mPTQueue.put([1, threading.Thread(target=orderThreadPrintA)])
mPTQueue.put([3, threading.Thread(target=orderThreadPrintB)])
mPTQueue.put([2, threading.Thread(target=orderThreadPrintC)])

while not mPTQueue.empty():
    print(mPTQueue.get())

mCond = threading.Condition()


def notifyWait():
    mCond.acquire()
    try:
        mCond.wait()
        print("Wating...")
    finally:
        mCond.release()


def notifySingle():
    mCond.acquire()
    try:
        mCond.notify()
        # mCond.notifyAll()
        print("Notifing...")
    finally:
        mCond.release()


t1 = threading.Thread(target=notifyWait)
t2 = threading.Thread(target=notifySingle)
t3 = threading.Thread(target=notifySingle)

t1.start()
t2.start()
t3.start()
