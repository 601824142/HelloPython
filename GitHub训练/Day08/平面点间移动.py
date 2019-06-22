# coding=utf-8
"""
   作者:万星明
   类名:
   注释:定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
   日期:2019/6/22 15:05
"""
from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法"""
        # 横坐标
        self.x = x
        # 纵坐标
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置"""
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量"""
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离"""
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s,%s)' % (str(self.x), str(self.y))


def main():
    point01 = Point(3, 5)
    point02 = Point()
    # 输出点坐标
    print(point01.__str__())
    print(point02.__str__())
    # 移动点显示坐标
    point02.move_by(-1, 3)
    print(point02.__str__())
    # 计算两点距离
    print(point01.distance_to(point02))


if __name__ == '__main__':
    main()
