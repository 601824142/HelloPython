# coding=utf-8
"""
   作者:万星明
   类名:运行常用模块
   注释:Python常用模块
        - 运行时服务相关模块: copy / pickle / sys / ...
        - 数学相关模块: decimal / math / random / ...
        - 字符串处理模块: codecs / re / ...
        - 文件处理相关模块: shutil / gzip / ...
        - 操作系统服务相关模块: datetime / os / time / logging / io / ...
        - 进程和线程相关模块: multiprocessing / threading / queue
        - 网络应用相关模块: ftplib / http / smtplib / urllib / ...
        - Web编程相关模块: cgi / webbrowser
        - 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...
   日期:2019/6/12 20:33
"""

import time
import shutil
import os

# 当前时间戳
seconds = time.time()
print(seconds)

# 格式化时间戳为本地的时间。 如果sec参数未输入，则以当前时间为转换标准
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
# asctime = time.asctime(localtime)
# print(asctime)
# strtime = time.strftime('%Y-%m-%d %H:%M:%S', localtime)
# print(strtime)
# mydate = time.strptime('2018-1-1', '%Y-%m-%d')
# print(mydate)
#
# shutil.copy('/Users/Hao/hello.py', '/Users/Hao/Desktop/first.py')
# os.system('ls -l')
# os.chdir('/Users/Hao')
# os.system('ls -l')
# os.mkdir('test')