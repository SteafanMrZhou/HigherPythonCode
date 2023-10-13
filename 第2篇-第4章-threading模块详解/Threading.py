import ctypes
import inspect
import os
import threading
import time


def tHello():
    print("hello Threading")


mThread = threading.Thread(target=tHello)
mThread.start()


class subThread(threading.Thread):

    def __init__(self):
        super().__init__()

    def run(self):
        print('thread %s is running.' % (threading.current_thread().name))
        print('thread %s end.' % (threading.current_thread().name))


print('thread %s is running.' % (threading.current_thread().name))

mThread = subThread()
mThread.start()


def exp_raise(tid, exctype):
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("无效的线程ID")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("加载线程管理器失败")


def stop_thread(thread):
    exp_raise(thread.ident, SystemExit)


def get_thread():
    pid = os.getpid()
    while True:
        ts = threading.enumerate()
        print('------- Running threads On Pid: %d -------' % pid)
        for t in ts:
            print(t.name, t.ident, t.is_alive())
            if t.name == 'Thread-test2':
                print('---------------------------------')
                stop_thread(t)
        time.sleep(1)
