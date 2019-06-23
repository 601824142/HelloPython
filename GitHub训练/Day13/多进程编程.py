# coding=utf-8
"""
  名称:多进程编程
  作者:万星明
  时间:2019/6/23 16:57
  注释:
"""
from multiprocessing import Process
from os import getpid
from random import randint
from time import sleep, time


# 单线程
def download(filename):
    print("开始下载%s....." % filename)
    # 随机数
    sleep_time = randint(5, 10)
    sleep(sleep_time)
    print("%s下载完成!耗费了%d秒" % (filename, sleep_time))


# 多线程
def download_task(filename):
    print('启动下载进程,进程号[%d].' % getpid())
    print("开始下载%s....." % filename)
    # 随机数
    sleep_time = randint(5, 10)
    sleep(sleep_time)
    print("%s下载完成!耗费了%d秒" % (filename, sleep_time))


def test01():
    start = time()
    download('Python程序设计.PDF')
    download('Java程序设计.PDF')
    end = time()

    print('总共时长:%.2f秒' % (end - start))


def test02():
    start = time()
    # 创建进程1
    process01 = Process(target=download_task, args=('Python程序设计.PDF',))
    process01.start()

    # 创建进程2
    process02 = Process(target=download_task, args=('Java程序设计.PDF',))
    process02.start()

    # 将两个线程加入主线程
    process01.join()
    process02.join()
    end = time()

    print('总共时长:%.2f秒' % (end - start))


if __name__ == '__main__':
    test02()