# 1、定义一个计数器变量,从数字1开始,循环会比较方便
row = 1
# 2、开始循环
while row <= 5:

    col = 1
    while col <= row:
        print("*", end="")
        col += 1
    print("")
    # print("*" * row)
    row += 1
