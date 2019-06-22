# coding=utf-8
"""
   作者:万星明
   类名:
   注释:定义和使用集合
   日期:2019/6/22 10:46
"""


def main():
    # 定义集合
    set1 = {1, 2, 3, 3, 3, 2}
    print(set1)
    set1.add(4)
    set1.add(5)
    print(set1)
    print('集合长度:', len(set1))

    # 定义集合
    set2 = set(range(1, 10))
    print(set2)
    set2.update([11, 12])
    print(set2)
    set2.discard(5)

    # 将元素从集合中删除
    if 4 in set2:
        set2.remove(4)
    print(set2)

    # 遍历集合容器
    for elem in set2:
        print(elem ** 2, end=' ')
    print()

    # 将元组转换成集合
    set3 = set((1, 2, 3, 3, 2, 1))
    print(set3.pop())
    print(set3)


if __name__ == '__main__':
    main()
