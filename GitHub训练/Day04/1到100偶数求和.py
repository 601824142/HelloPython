# coding=utf-8
"""
   作者:万星明
   类名:1到100偶数和
   注释:1到100偶数和
   日期:2019/5/13 20:37
"""
# for循环实现偶数求和
sum = 0
for x in range(2, 101, 2):
    sum += x

print(sum)


# while循环实现偶数求和
sum = 0
num = 2
while num <= 100:
    sum += num
    num += 2
print(sum)