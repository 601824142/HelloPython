# coding=utf-8
"""
   作者:万星明
   类名:
   注释:属性装饰器
   日期:2019/6/22 16:48
"""


class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器——getter方法
    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    # 修改器——setter方法
    @name.setter
    def name(self, name):
        self._name = name

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋。' % self._name)
        else:
            print('%s正在玩斗地主。' % self._name)



class Car(object):
    """车类"""
    def __init__(self, brand, max_speed):
        self.set_brand(brand)
        self.set_max_speed(max_speed)

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        self._brand = brand

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('max_speed参数错误')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)

    # 用已有的修改器和访问器定义属性
    brand = property(get_brand, set_brand)
    max_speed = property(get_max_speed, set_max_speed)








def main():
    # person = Person('万星明', 24)
    # person.play()
    #
    # person.age = 14
    # person.play()
    #
    # person.name = "朱秀娟"
    # person.play()

    car = Car('QQ', 120)
    print(car)
    # ValueError
    # car.max_speed = -100
    car.max_speed = 320
    car.brand = "Benz"
    print(car)
    print(Car.brand)
    print(Car.brand.fget)
    print(Car.brand.fset)


if __name__ == '__main__':
    main()


