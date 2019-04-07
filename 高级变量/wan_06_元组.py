# coding=utf-8
"""作者:万星明"""

info_tuple = ("wan", 179, 24)
print(type(info_tuple))

# 取值与索引
print(info_tuple[0])
# 知道数据内容,查询索引
print(info_tuple.index("wan"))

# 统计计数
print(info_tuple.count("wan"))
# 求长度
print(len(info_tuple))
