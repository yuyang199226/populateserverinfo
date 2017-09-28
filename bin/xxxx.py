import threading
import time,random
# class TimerClass(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.event = threading.Event()
#
#     def run(self):
#         while not self.event.is_set():
#             print("something")
#             self.event.wait(2)
# thread = TimerClass()
# thread.start()
import threading
import time,random
# event=threading.Event()
# def foo():
#     time.sleep(1)
#     print("first>>>")
# def bar():
#     sum = 0
#     for i in range (10):
#         sum+=i
#     print(sum)
#     # event.set()
# t1=threading.Thread(target=foo)
# t2=threading.Thread(target=bar)
# t1.setDaemon(True)
# t2.setDaemon(True)
# t1.start()
#
# t2.start()

# print('done')
# import queue
# q=queue.LifoQueue()
# for i in range(0,4):
#     q.put(i)
# while not q.empty():
#     a = q.get()
#     print(a)
import threading
import time

#
# def sayhi(num):  # 定义每个线程要运行的函数
#
#     print("running on number:%s" % num)
#
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
#     t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例
#
#     t1.start()  # 启动线程
#     t2.start()  # 启动另一个线程
#
#     print(t1.getName())  # 获取线程名
#     print(t2.getName())


# class MyThread(threading.Thread):
#     def __init__(self, num):
#         threading.Thread.__init__(self)
#         self.num = num
#     # num=2
#     def run(self):  # 定义每个线程要运行的函数
#
#         print("running on number:%s" % self.num)
#
#         time.sleep(3)
#
#
# if __name__ == '__main__':
#     t1 = MyThread(1)
#     t2 = MyThread(2)
#     t1.start()
#     t2.start()
import time
import threading

#
# def run(n):
#     print('[%s]------running----\n' % n)
#     time.sleep(2)
#     print('--done--')
#
#
# def main():
#     for i in range(5):
#         t = threading.Thread(target=run, args=[i, ])
#         t.start()
#         t.join(1)
#         print('starting thread', t.getName())
#
#
# m = threading.Thread(target=main, args=[])
# m.setDaemon(True)  # 将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
# m.start()
# m.join(timeout=2)
# print("---main thread done----")
import json
from collections import OrderedDict
a=[(121, 900), (124, 500), (123, 400), (126, 100)]

b={121: 900, 124: 500, 123: 400, 126: 100}
dic=OrderedDict()
for i in a:
    dic[i[0]]=i[1]
d=json.dumps(dic)
print(d)
