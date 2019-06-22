# coding=utf-8
"""
   作者:万星明
   类名:内置函数
   注释:Python的内置函数
        - 数学相关: abs / divmod / pow / round / min / max / sum
        - 序列相关: len / range / next / filter / map / sorted / slice / reversed
        - 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
        - 数据结构: dict / list / set / tuple
        - 其他函数: all / any / id / input / open / print / type
   日期:2019/6/12 20:18
"""


def myFilter(my_str):
    return len(my_str) == 6


print(chr(0x1a32))
print(hex(ord('骆')))
print(abs(-1.2345))
print(round(-1.2345))
print(pow(1.2345, 5))
fruits = ['orange', 'peach', 'durian', 'watermelon']
print(fruits[slice(1, 3)])
fruits2 = list(filter(myFilter, fruits))
print(fruits)
print(fruits2)