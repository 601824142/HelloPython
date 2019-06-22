# coding=utf-8
"""
   作者:万星明
   类名:
   注释:对父类已有的方法给出新的实现版本,这个动作称之为方法重写(override)
   日期:2019/6/22 17:42
"""
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物虚类抽象类"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s:汪汪汪。。。' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s:喵喵喵。。。' % self._nickname)


if __name__ == '__main__':
    pets = [Dog('旺财'), Cat('汤姆')]
    for pet in pets:
        pet.make_voice()

