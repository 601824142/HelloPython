# 计算0-100之间所有数字的累计求和结果
# 1、定义一个整数的变量记录循环的次数
result = 0
i = 0

# 2、开始循环
while i <= 100:
    print(i)
    result += i
    # 处理计数器
    i += 1

print("和：%d" % result)
