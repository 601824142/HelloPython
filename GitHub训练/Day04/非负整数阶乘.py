# coding=utf-8
"""
   作者:万星明
   类名:非负整数阶乘
   注释:输入非负整数n计算n!
   日期:2019/5/13 20:39
"""

n = int(input("n = "))
result = 1
for x in range(1, n + 1):
    result *= x

print("%d! = %d" % (n, result))
