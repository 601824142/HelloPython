# coding=utf-8
"""
   作者:万星明
   类名:
   注释:类属性私有化
   日期:2019/6/22 14:35
"""


class Test:

    def __init__(self, foo):
        # 私有化属性
        self.__foo = foo

    # 私有化方法
    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    # 调用私有化方法
    test._Test__bar()
    # 调用私有化属性
    print(test._Test__foo)


if __name__ == "__main__":
    main()
