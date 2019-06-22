# coding=utf-8
"""
   作者:万星明
   类名:最大公约最小公倍数
   注释:最大公约最小公倍数
   日期:2019/6/12 20:09
"""


def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 1, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
    return 1


def lcm(x, y):
    return x * y // gcd(x, y)


print(gcd(15, 27))
print(lcm(15, 27))
