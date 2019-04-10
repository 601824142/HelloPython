# coding=utf-8
"""作者:万星明"""

poem = ["登黄鹤楼  ",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    # 去除空白
    poem_str = poem_str.strip(" ")

    # 居中
    # print("|%s|" % poem_str.center(10, "　"))

    # 居左
    print("|%s|" % poem_str.ljust(10, "　"))
