# coding=utf-8
"""
  名称:构成三角形
  作者:万星明
  时间:2019/5/12 23:13
  注释:判断输入的边长能否构成三角形,如果能则计算出三角形的周长和面积
"""
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("可以构成三角形,周长为:%f" % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("面积为:%f" % area)
else:
    print("无法构成三角形！")
