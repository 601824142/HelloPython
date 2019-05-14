# coding=utf-8
"""
   作者:万星明
   类名:1到100求和
   注释:1到100求和
   日期:2019/5/13 20:33
"""
# for循环实现求和
total = 0

for x in range(1, 101):
    total += x

print(total)


# while循环求和

sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print(sum)