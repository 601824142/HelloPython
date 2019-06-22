# coding=utf-8
"""
   作者:万星明
   类名:
   注释:属性限定绑定
   日期:2019/6/22 16:58
"""


class Person(object):
    # 限定该对象只能绑定_name,_age,_sex属性
    __slots__ = ('_name', '_age', '_sex')

    def __init__(self, name, age, sex):
        """初始化"""
        self._name = name
        self._age = age
        self._sex = sex

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s(%s)正在玩飞行棋。' % (self._name, self._sex))
        else:
            print('%s(%s)正在玩斗地主。' % (self._name, self._sex))


def main():
    person = Person('万星明', 24, '男')
    person.play()

    person.age = 14
    person.play()

    person.name = "朱秀娟"
    person.play()


if __name__ == '__main__':
    main()
