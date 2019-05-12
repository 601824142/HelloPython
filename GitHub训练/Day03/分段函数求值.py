# coding=utf-8
"""
  名称:分段函数求值
  作者:万星明
  时间:2019/5/12 22:49
  注释:
                3x - 5  (x > 1)
        f(x) =  x + 2   (-1 <= x <= 1)
                5x + 3  (x < -1)
"""
x = float(input("x = "))

if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3

print("f(%.2f) = %.2f" % (x, y))
