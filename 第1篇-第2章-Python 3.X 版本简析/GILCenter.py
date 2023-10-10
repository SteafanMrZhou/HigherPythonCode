import threading
import time
import sys


def readFile():
    print("线程：" + str(threading.current_thread().name) + "开始执行")
    start = time.time()
    with open('gilText.txt', 'r') as f:
        data = f.read()
        print(data)
    end = time.time()
    print(end - start)


t1 = threading.Thread(target=readFile)
t2 = threading.Thread(target=readFile)

t1.start()
t2.start()

print(sys.flags.nogil)
