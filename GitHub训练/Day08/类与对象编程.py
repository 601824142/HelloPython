# coding=utf-8
"""
   作者:万星明
   类名:
   注释:类与对象
   日期:2019/6/22 14:23
"""


class Student(object):

    # 特殊方法,初始化对象操作,绑定name与age属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义学习方法
    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # 日常活动方法
    def do_what(self):
        if self.age < 18:
            print('%s只能写作业.' % self.name)
        else:
            print('%s可以看电影.' % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    student01 = Student('万星明', 24)
    # 对象进行学习
    student01.study('Python')
    # 对象进行活动
    student01.do_what()

    student02 = Student('朱秀娟', 12)
    student02.study('特效制作')
    student02.do_what()


if __name__ == '__main__':
    main()
