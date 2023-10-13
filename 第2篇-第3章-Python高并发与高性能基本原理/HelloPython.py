import sys

a = 1
b = 2.5
c = [{"a", "b", "c"}]


def hello():
    print(a + b)
    print(sys.getrefcount(a))
    print(c)


hello()
