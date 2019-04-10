# coding=utf-8
"""作者:万星明"""

hello_str = "hello world"

# 1.判断是否以指定字符串开始
print(hello_str.startswith("hello"))

# 2.判断是否以指定字符串结束
print(hello_str.endswith("world"))

# 3.查找指定字符串,当查找的字符串不存在时：find返回-1;index报错
print(hello_str.find("llo"))
print(hello_str.find("aaa"))
# print(hello_str.index("abc"))

# 4.替换字符串
hello_str = hello_str.replace("world", "python")
print(hello_str)