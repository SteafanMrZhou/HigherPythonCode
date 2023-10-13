import threading

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
    mCond.notify()
    print("Notifing...")


t1 = threading.Thread(target=notifyWait)
t2 = threading.Thread(target=notifySingle)

t1.start()
t2.start()
