import threading


global a
for i in range(1000000):
    a += 1
    # threading.Lock.acquire()
    # a += 1
    # threading.Lock.release()

print(a)
