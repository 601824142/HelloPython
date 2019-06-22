# coding=utf-8
"""
   作者:万星明
   类名:
   注释:定义一个类描述数字时钟
   日期:2019/6/22 14:47
"""
from time import sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法"""
        self._hour = hour
        self._minute = minute
        self._second = second

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
    clock = Clock(23, 59, 30)
    while True:
        print(clock.__display__())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
