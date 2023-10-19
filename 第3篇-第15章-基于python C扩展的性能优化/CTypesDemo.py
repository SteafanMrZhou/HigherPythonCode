import ctypes
from threading import Thread
from ctypes.util import find_library
from distutils.core import setup, Extension

libm = ctypes.cdll.LoadLibrary(find_library('m'))

libm.cos.argtypes = [ctypes.c_double]
libm.cos.restype = ctypes.c_double


def cos_func(arg):
    return libm.cos(arg)


setup(ext_modules=[Extension("_cos_module",
                             sources=["cos_module.c", "cos_module.i"])])

stduLib = ctypes.cdll.LoadLibrary("scrapy_thread_deal_up.so")
t = Thread(target=stduLib.scrapy_tips_conetnt_by_cthread)
t.start()

stduLib.scrapy_tips_conetnt_by_cthread
