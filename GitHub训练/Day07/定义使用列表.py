# coding=utf-8
"""
   作者:万星明
   类名:定义使用列表
   注释:- 用下标访问元素
       - 添加元素
       - 删除元素
   日期:2019/6/22 9:55
"""


def main():
    fruits = ['grape', 'apple', 'strawberry']
    print(fruits)
    # 通过下标访问元素
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])

    # 修改
    fruits[1] = 'banana'
    print(fruits)

    # 添加元素
    fruits.append("organ")
    fruits.insert(0, "watermelon")
    print(fruits)

    # 删除元素
    del fruits[1]
    fruits.pop()
    fruits.pop(0)
    fruits.remove('strawberry')
    print(fruits)


if __name__ == '__main__':
    main()
