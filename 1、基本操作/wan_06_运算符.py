# 定义常量
a = 21
b = 10
c = 0

# 计算a+b赋值给c
# c = a + b
# print("1、c的值为：", c)


# 计算a-b赋值给c
# c = a - b
# print("2、c的值为：", c)


# 计算a*b赋值给c
# c = a * b
# print("3、c的值为：", c)


# 计算a/b赋值给c
# c = a / b
# print("4、c的值为：", c)

# 计算a%b赋值给c
# c = a % b
# print("5、c的值为：", c)


# 两个*代表幂次
# a = 2
# b = 3
# c = a ** b
# print("6、c的值为：", c)


# 两个/代表除取整
# a = 7
# b = 4
# c = a // b
# print("7、c的值为：", c)


# if逻辑判断
# a = 21
# b = 10
# c = 0
# if a == b:
#     print("1、a等于b")
# else:
#     print("1、a不等于b")
#
# if a != b:
#     print("2、a不等于b")
# else:
#     print("2、a等于b")
#
# if a < b:
#     print("3、a小于b")
# else:
#     print("3、a大于等于b")
#
# if a > b:
#     print("4、a大于b")
# else:
#     print("4、a小于等于b")



# 修改变量 a 和 b 的值
# a = 5
# b = 20
# if a <= b:
#     print("5、a小于等于b")
# else:
#     print("5、a大于b")
#
# if b >= a:
#     print("6、b大于等于a")
# else:
#     print("6、b小于a")



# 计算值
# a = 21
# b = 10
# c = 0
#
# c = a + b
# print("1、c的值为：", c)
# c += a
# print("2、c的值为：", c)
# c *= a
# print("3、c的值为：", c)
# c /= a
# print("4、c的值为：", c)
#
# c = 2
# c %= a
# print("5、c的值为：", c)
# c **= a
# print("6、c的值为：", c)
# c //= a
# print("7、c的值为：", c)


# 位运算
# a = 60  # 60 = 0011 1100
# b = 13  # 13 = 0000 1101
# c = 0
#
# c = a & b  # 12 = 0000 1100
# print("1、c的值为：", c)
#
# c = a | b  # 61 = 0011 1101
# print("2、c的值为：", c)
#
# c = a ^ b  # 49 = 0011 0001
# print("3、c的值为：", c)
#
# c = ~a  # -61 = 1100 0011
# print("4、c的值为：", c)
#
# c = a << 2  # 240 = 1111 0000
# print("5、c的值为：", c)
#
# c = a >> 2  # 15 = 0000 1111
# print("6、c的值为：", c)



# 逻辑判断
a = 10
b = 20

if a and b:
    print("1、变量a和b都为 true")
else:
    print("1、变量a和b有一个不为 true")

if a or b:
    print("2、变量a和b都为 true，或其中一个变量为 true")
else:
    print("2、变量a和b都不为 true")

# 修改变量a的值
a = 0
if a and b:
    print("3、变量a和b都为 true")
else:
    print("3、变量a和b有一个不为 true")

if a or b:
    print("4、变量a和b都为 true，或其中一个变量为 true")
else:
    print("4、变量a和b都不为 true")

if not (a and b):
    print("5、变量a和b都为 false，或其中一个变量为 false")
else:
    print("5、变量a和b都为 true")


# a = 10
# b = 20
# tlist = [1, 2, 3, 4, 5]
#
# if a in tlist:
#     print("1 - 变量 a 在给定的列表中 list 中")
# else:
#     print("1 - 变量 a 不在给定的列表中 list 中")
#
# if b not in tlist:
#     print("2 - 变量 b 不在给定的列表中 list 中")
# else:
#     print("2 - 变量 b 在给定的列表中 list 中")
#
# # 修改变量 a 的值
# a = 2
# if a in tlist:
#     print("3 - 变量 a 在给定的列表中 list 中")
# else:
#     print("3 - 变量 a 不在给定的列表中 list 中")


# a = 20
# # b = 20
# #
# # if a is b:
# #     print("1 - a 和 b 有相同的标识")
# # else:
# #     print("1 - a 和 b 没有相同的标识")
# #
# # if id(a) == id(b):
# #     print("2 - a 和 b 有相同的标识")
# # else:
# #     print("2 - a 和 b 没有相同的标识")
# #
# # # 修改变量 b 的值
# # b = 30
# # if a is b:
# #     print("3 - a 和 b 有相同的标识")
# # else:
# #     print("3 - a 和 b 没有相同的标识")
# #
# # if a is not b:
# #     print("4 - a 和 b 没有相同的标识")
# # else:
# #     print("4 - a 和 b 有相同的标识")


# a = [1, 2, 3]
# b = a
# print(b is a)
# print(b == a)
#
# b = a[:]
# print(b is a)
# print(b == a)


# a = 20
# b = 10
# c = 15
# d = 5
# e = 0
#
# e = (a + b) * c / d  # ( 30 * 15 ) / 5
# print("(a + b) * c / d 运算结果为：", e)
#
# e = ((a + b) * c) / d  # (30 * 15 ) / 5
# print("((a + b) * c) / d 运算结果为：", e)
#
# e = (a + b) * (c / d);  # (30) * (15/5)
# print("(a + b) * (c / d) 运算结果为：", e)
#
# e = a + (b * c) / d;  # 20 + (150/5)
# print("a + (b * c) / d 运算结果为：", e)

