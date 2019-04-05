# coding=utf-8
"""作者:万星明"""
import keyword

name_list = ["万星明", "朱秀娟", "万星月", "朱秀媛"]
num_list = [6, 8, 2, 4, 1, 10]

# 升序
# name_list.sort()
# num_list.sort()


# 降序
# name_list.sort(reverse=True)
# num_list.sort(reverse=True)


# 逆序(反转)
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)
print(keyword.kwlist)