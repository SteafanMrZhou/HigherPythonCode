def atomicVariablesDemo():
    mList = []
    mList.append(123)
    print(mList)


def atomicVariablesDemo2():
    mList = []
    x = 0
    mList.append(123)
    mList.append(456)
    mList.append(789)
    for i in range(len(mList)):
        x = mList[2]
    print(x)


def atomicVariablesDemo3():
    x = 0
    y = 2
    x = y
    print(x)
    print(y)


def atomicVariablesDemo4():
    mList = {'x': 1, 'y': 2}
    y = 3
    mList['x'] = y
    print(mList)
