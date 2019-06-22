# coding=utf-8
"""
   作者:万星明
   类名:
   注释:静态方法和类方法
   日期:2019/6/22 17:08
"""
from math import sqrt


class Triangle(object):
    """三角形"""

    __slots__ = ('_a', '_b', '_c')

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))


def main():
    a, b, c = 3, 4, 5

    # 静态方法调用
    if Triangle.is_valid(a, b, c):
        triangle = Triangle(a, b, c)
        print("三角形周长:%s" % triangle.perimeter())
        print("三角形周长:%s" % Triangle.perimeter(triangle))
        print("三角形面积:%s" % triangle.area())
        print("三角形面积:%s" % Triangle.area(triangle))
    else:
        print("无法构成三角形!")


if __name__ == '__main__':
    main()
