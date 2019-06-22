# coding=utf-8
"""
   作者:万星明
   类名:
   注释:字典的常用操作
   日期:2019/6/22 9:19
"""


def main():
    stu = {'name': '万星明', 'age': 24, 'sex': '男'}

    print("定义的字典:%s" % stu)
    print("定义的字典键:%s" % stu.keys())
    print("定义的字典值:%s" % stu.values())

    print("定义的字典元组列表:%s" % stu.items())
    for elem in stu.items():
        print(elem)
        print(elem[0], elem[1])
    if 'age' in stu:
        stu['age'] = 18
    print(stu)
    stu.setdefault('score', 60)
    print(stu)
    stu.setdefault('score', 100)
    print(stu)
    stu['score'] = 100
    print(stu)


if __name__ == '__main__':
    main()
