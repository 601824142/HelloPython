# coding=utf-8
"""
   作者:万星明
   类名:
   注释:在类中定义类方法,类方法的第一个参数约定名为cls
   日期:2019/6/22 17:21
"""
from time import localtime, time, sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """时分秒"""
        self._hour = hour
        self._minute = minute
        self._second = second

    # 类方法
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """时间规则"""
        # 每运行一秒
        self._second += 1
        # 如果运行了60秒
        if self._second == 60:
            # 将秒针赋值为0
            self._second = 0
            # 分针进1
            self._minute += 1
            # 如果运行了60分
            if self._minute == 60:
                # 将分针赋值为0
                self._minute = 0
                # 时针进1
                self._hour += 1
                # 如果运行了24小时
                if self._hour == 24:
                    # 时针赋值为0
                    self._hour = 0

    def __display__(self):
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


def main():
    # 通过类方法创建对象并拿到系统时间
    clock = Clock.now()
    while True:
        print(clock.__display__())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
