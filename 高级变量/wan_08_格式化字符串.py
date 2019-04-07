# coding=utf-8
"""作者:万星明"""

info_tuple = ("万星明", 24, 1.79)

# 格式化字符串后面得‘()’本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple

print(info_str)

# 列表和元组之间互相转换
a_list = list(info_tuple)
print(a_list)

b_tuple = tuple(a_list)
print(b_tuple)