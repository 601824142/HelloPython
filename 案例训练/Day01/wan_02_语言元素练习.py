# coding=utf-8
import math

# 1、将华氏温度转换为摄氏温度
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))


# 2、输入半径计算圆的周长和面积
radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.5f' % perimeter)
print('面积: %.5f' % area)


# 3、输入年份 如果是闰年输出True 否则输出False
year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)