# coding=utf-8
"""
   作者:万星明
   类名:factorial
   注释:阶乘函数
   日期:2019/6/12 20:06
"""


def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(factorial(6))
