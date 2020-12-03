# 变量定义
# a = b = c = 1
# a, b, c = 1, 2, "python"
# print(a)
# print(b)
# print(c)


# 变量类型
# a, b, c, d = 20, 5.5, True, 4 + 3j
# print(type(a), type(b), type(c), type(d))


# 判断变量类型
# e = 111
# print(isinstance(e, bool))


# 计算
# print(5 + 4)
# print(4.3 - 2)
# print(3 * 7)
# print(2 / 4)
# print(2 // 4)
# print(17 % 3)
# print(2 ** 3)


# 字符串输出
# str = 'python'
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + "TEST")  # 连接字符串
# print(r"pytho\nn")


# 列表处理
# aaa = ['abcd', 786, 2.23, 'runoob', 70.2]
# bbb = [123, 'runoob']
# print(aaa)  # 输出完整列表
# print(aaa[0])  # 输出列表第一个元素
# print(aaa[1:3])  # 从第二个开始输出到第三个元素
# print(aaa[2:])  # 输出从第三个元素开始的所有元素
# print(bbb * 2)  # 输出两次列表
# print(aaa + bbb)  # 连接列表


# 数组处理
# a = [1, 2, 3, 4, 5, 6]
# a[0] = 9
# a[2:5] = [13, 14, 15]
# print(a)


# 元组处理
# tup = ('abcd', 786, 2.23, 'runoob', 70.2)
# tintup = (123, 'runoob')
# print(tup)  # 输出完整元组
# print(tup[0])  # 输出元组的第一个元素
# print(tup[1:3])  # 输出从第二个元素开始到第三个元素
# print(tup[2:])  # 输出从第三个元素开始的所有元素
# print(tintup * 2)  # 输出两次元组
# print(tup + tintup)  # 连接元组


# 集合(特性：不可重复)
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print(student)  # 输出集合，重复的元素被自动去掉


# 成员测试:判断元素是否存在集合中
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# if 'Rose' in student:
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')


# set创建集合,可以进行集合运算
# a = set('abracadabra')
# b = set('alacazam')
# print(a)
# print(a - b)  # a 和 b 的差集
# print(a | b)  # a 和 b 的并集
# print(a & b)  # a 和 b 的交集
# print(a ^ b)  # a 和 b 中不同时存在的元素


# 字典
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

