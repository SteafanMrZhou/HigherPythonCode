import gc
import objgraph


class A(object):
    def __init__(self):
        self.child = None

    def destroy(self):
        self.child = None


class B(object):
    def __init__(self):
        self.parent = None

    def destroy(self):
        self.parent = None


x = None

class Lazarus:

    def __del__(self):
        global x
        x = self


lazarus = Lazarus()
gc.is_finalized(lazarus)


def test3():
    a = A()
    b = B()
    a.child = b
    b.parent = a
    a.destroy()
    b.destroy()


def test4():
    gc.set_threshold(3000)
    gc.get_threshold()


test3()
print('Object count of A:', objgraph.count('A'))
print('Object count of B:', objgraph.count('B'))
