# coding=utf-8
"""
   作者:万星明
   类名:
   注释:定义与使用圆形
   日期:2019/6/22 16:20
"""
import math


class Circle(object):
    """圆形"""

    def __init__(self, radius):
        """初始化"""
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def perimeter(self):
        return 2 * math.pi * self._radius

    @property
    def area(self):
        return math.pi * self._radius * self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius if radius > 0 else 0


if __name__ == '__main__':
    # 创建圆形
    small = Circle(float(input('请输入半径:')))
    # 圆形加大
    big = Circle(small.radius+3)

    print('围墙的造价为: ￥%.1f元' % (big.perimeter * 115))
    print('过道的造价为: ￥%.1f元' % ((big.area - small.area) * 65))