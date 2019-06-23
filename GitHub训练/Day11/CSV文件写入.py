# coding=utf-8
"""
  名称:CSV文件写入
  作者:万星明
  时间:2019/6/23 15:58
  注释:
"""
import csv


class Person(object):
    """人类"""

    __slots__ = ('_name', '_age', '_sex')

    def __init__(self, name, age, sex):
        self._name = name
        self._age = age
        self._sex = sex

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def sex(self):
        return self._sex

    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    @sex.setter
    def sex(self, sex):
        self._sex = sex


def main():
    filename = 'sources/person.csv'
    persons = [Person('万星明', 24, '男'), Person('朱秀娟', 23, '女')]

    try:
        with open(filename, 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for person in persons:
                writer.writerow([person.name, person.age, person.sex])
    except BaseException as e:
        print("无法写入文件:%s" % e, filename)
    else:
        print("保存数据完成!")


if __name__ == '__main__':
    main()
