# coding=utf-8
"""
   作者:万星明
   类名:判断素数
   注释:输入一个正整数判断它是不是素数
   日期:2019/5/13 20:42
"""

from math import sqrt

num = int(input("请输入需要判断的正整数:"))
end = int(sqrt(num))
is_prime = True

for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print("%d是素数!" % num)
else:
    print("%d不是素数!" % num)
