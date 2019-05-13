# coding=utf-8
"""
   作者:万星明
   类名:计算最大公约数和最小公倍数
   注释:输入两个正整数计算最大公约数和最小公倍数
   日期:2019/5/13 20:47
"""

x = int(input("x = "))
y = int(input("y = "))

if x > y:
    (x, y) = (y, x)

for facotr in range(x, 0, -1):
    if x % facotr == 0 and y % facotr == 0:
        print("%d和%d的最大公约数是%d" % (x, y, facotr))
        print("%d和%d的最小公倍数是%d" % (x, y, x * y // facotr))
        break
