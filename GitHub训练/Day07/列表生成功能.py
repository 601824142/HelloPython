# coding=utf-8
"""
   作者:万星明
   类名:
   注释:生成列表
   日期:2019/6/22 10:28
"""


# 生成斐波那契数列的生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    # 用Range创建随机数值
    list1 = list(range(1, 11))
    print(list1)

    # 生成表达式
    list2 = [x * x for x in range(1, 11)]
    print(list2)

    list3 = [m + n for m in 'ABCDEFG' for n in '12345']
    print(list3)
    print(len(list3))

    # 生成器(节省空间但生成下一个元素时需要花费时间)
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print(gen)

    for elem in gen:
        print(elem, end=" ")
    print()

    gen = fib(20)
    print(gen)

    for elem in gen:
        print(elem, end=" ")
    print()


if __name__ == '__main__':
    main()
