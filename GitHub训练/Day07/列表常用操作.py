# coding=utf-8
"""
   作者:万星明
   类名:列表常用操作
   注释:列表常用操作
        - 列表连接
        - 获取长度
        - 遍历列表
        - 列表切片
        - 列表排序
        - 列表反转
        - 查找元素
   日期:2019/6/22 9:46
"""


def main():
    fruits = ['grape', 'apple']
    fruits += ['mango']

    # 循环遍历列表
    for fruit in fruits:
        print(fruit.title(), end=' ')
    print()

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)

    fruits3 = fruits[:]
    print(fruits3)

    fruits4 = fruits[-3:-1]
    print(fruits4)

    fruits5 = fruits[::-1]
    print(fruits5)


if __name__ == '__main__':
    main()
