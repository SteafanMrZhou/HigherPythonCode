import datetime
import logging
import sys


def allocateCommondMemory(self, commondDesc, parameterDesc):
    if commondDesc == "print":
        startTime = datetime.datetime.now()
        print("print指令打印内容:" + parameterDesc)
        endTime = datetime.datetime.now()
        duringTime = endTime - startTime
        print("print指令执行完毕所消耗时间(微秒):" + str(duringTime.microseconds))
        print("print指令打印内容为:" + str(parameterDesc) + "，所占内存空间为:" + str(sys.getsizeof(parameterDesc)) + "字节")
        memoryOfPrint = sys.getsizeof(print())
        memoryOfParameter = sys.getsizeof(parameterDesc)
        print("print指令执行完成上述任务所占用总内存大小为:" + str(memoryOfParameter + memoryOfPrint))
        print("print指令本身所占内存空间：" + str(sys.getsizeof(print())) + "字节")


def allocateLogMemory(self):
    logStr = "this is a debug level info"
    startTime = datetime.datetime.now()
    logging.debug(logStr)
    endTime = datetime.datetime.now()
    duringTime = endTime - startTime
    print("Logging打印Debug级别日志所需时间为：" + str(duringTime.microseconds) + "微秒")
    memoryOfLoggingDebug = sys.getsizeof(logging.debug(""))
    print("Logging打印Debug级别日志本身所需内存为：" + str(memoryOfLoggingDebug) + "字节")
    memoryOfLogData = sys.getsizeof(logStr)
    print("Logging打印日志数据内存大小为：" + str(memoryOfLogData) + "字节")
    print("Logging打印Debug级别日志所需总内存为：" + str(memoryOfLoggingDebug + memoryOfLogData) + "字节")
