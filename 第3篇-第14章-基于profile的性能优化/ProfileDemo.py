import cProfile


def helloProfile():
    print("hello profile")


cProfile.run(helloProfile(), 'demo.txt')
