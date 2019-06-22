# coding=utf-8
"""
   作者:万星明
   类名:
   注释:另一种创建类的方式
   日期:2019/6/22 15:28
"""


def bar(self, name):
    self._name = name


def foo(self, course_name):
    print('%s正在学习%s.' % (self._name, course_name))


def main():
    Student = type('Student', (object,), dict(__init__=bar, study=foo))
    student01 = Student('万星明')
    student01.study('Python')


if __name__ == '__main__':
    main()
