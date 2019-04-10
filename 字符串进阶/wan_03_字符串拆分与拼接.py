# coding=utf-8
"""作者:万星明"""
poem = "登黄鹤楼\t王之涣\t白日依山尽\t黄河入海流\t欲穷千里目\t更上一层楼"

print(poem)

# 1.拆分字符串
poem_list = poem.split()
print(poem_list)

# 2.合并字符串
result = " ".join(poem_list)
print(result)