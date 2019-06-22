# coding=utf-8
"""
   作者:万星明
   类名:
   注释:找出列表中最大或最小的元素
   日期:2019/6/22 10:15
"""


def main():
    fruits = ['grape', 'apple', 'strawberry']
    # 直接使用内置的max和min函数找出列表中最大和最小元素
    # print(max(fruits))
    # print(min(fruits))

    # 自定义查询
    max_value = min_value = fruits[0]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]
        elif fruits[index] < min_value:
            min_value = fruits[index]
    print('Max:', max_value)
    print('Min:', min_value)


if __name__ == '__main__':
    main()
