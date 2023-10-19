import time


def forSimple():
    t1 = time.time()
    for i in range(10):
        print(i)
    t2 = time.time()

    print(t2 - t1)


def generatorSimple():
    t1 = time.time()
    testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(testList)):
        print(testList[i])
    t2 = time.time()
    print(t2 - t1)


forSimple()
generatorSimple()
