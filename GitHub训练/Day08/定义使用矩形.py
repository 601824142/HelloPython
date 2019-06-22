# coding=utf-8
"""
   作者:万星明
   类名:
   注释:定义和使用矩形类
   日期:2019/6/22 15:18
"""


class Rect(object):
    """矩形类"""

    def __init__(self, width=0, height=0):
        """初始化方法"""
        self.__width = width
        self.__height = height

    def perimeter(self):
        """计算周长"""
        return (self.__width + self.__height) * 2

    def area(self):
        """计算面积"""
        return self.__width * self.__height

    def __str__(self):
        """矩形对象的字符串表达形式"""
        return '矩形[%.2f,%.2f]' % (self.__width, self.__height)

    def __del__(self):
        """析构器"""
        print('销毁矩形对象')


if __name__ == '__main__':
    # 创建矩形对象
    rect01 = Rect()
    print(rect01)
    # 计算矩形周长与面积
    print(rect01.perimeter())
    print(rect01.area())

    rect02 = Rect(3.5, 4.5)
    print(rect02)
    print(rect02.perimeter())
    print(rect02.area())