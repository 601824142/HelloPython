# coding=utf-8
"""
  名称:打印三角形
  作者:万星明
  时间:2019/5/14 21:50
  注释:打印各种三角形图案
"""
row = int(input("请输入行数:"))
# for i in range(row):
#     for j in range(i + 1):
#         print("*", end=" ")
#     print()


# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()


for i in range(row):
    for j in range(row - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()