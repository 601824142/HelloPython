# coding=utf-8
"""
   作者:万星明
   类名:
   注释:定义使用元组
   日期:2019/6/22 11:39
"""


def main():
    # 定义元组
    man = ('万星明', 24, '男', '江西南昌')
    print(man)

    # 获取元组中的元素
    print(man[0])
    print(man[1])
    print(man[2])
    print(man[3])

    # 遍历元组中的值
    for member in man:
        print(member)

    # 重新给元组赋值(元组不支持更改,除非重新定义)
    # man[0] = '朱秀娟'
    # 变量man重新引用了新的元组 原来的元组被垃圾回收
    man = ('朱秀娟', 23, '女', '江西南昌')
    print(man)

    # 元组和列表的转换
    person = list(man)
    print(person)
    person[0] = '李小龙'
    person[1] = 25
    print(person)
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(fruits_tuple[1])


if __name__ == '__main__':
    main()
