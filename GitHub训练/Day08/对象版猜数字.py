# coding=utf-8
"""
   作者:万星明
   类名:
   注释:面向对象版本的猜数字游戏
   日期:2019/6/22 15:35
"""
from random import randint


class GuessMachine(object):
    """猜数字游戏"""

    def __init__(self):
        """初始化"""
        self.__answer = None
        self.__counter = None
        self.__hint = None

    def reset(self):
        self.__answer = randint(1, 100)
        self.__counter = 0
        self.__hint = None

    def guess(self, your_answer):
        self.__counter += 1
        if your_answer > self.__answer:
            self.__hint = '往小了猜'
        elif your_answer < self.__answer:
            self.__hint = '往大了猜'
        else:
            self.__hint = '恭喜你猜对了!'
            return True
        return False

    @property
    def counter(self):
        return self.__counter

    @property
    def hint(self):
        return self.__hint


if __name__ == '__main__':
    # 创建猜数字
    gm = GuessMachine()

    play_again = True
    # 当可以玩时
    while play_again:
        # 初始错误
        game_over = False
        # 当猜错时
        while not game_over:
            your_answer = int(input("请输入你猜的数字:"))
            game_over = gm.guess(your_answer)
            print(gm.hint)
            # 如果猜错判断猜的次数
            if not game_over:
                if gm.counter > 5:
                    print('智商不足,请及时充值!')
                    play_again = input('再玩一次?(y|n)') == 'y' or input('再玩一次?(y|n)') == 'Y'
                    # 初始数字
                    gm.reset()
            else:
                play_again = input('再玩一次?(y|n)') == 'y' or input('再玩一次?(y|n)') == 'Y'
                # 初始数字
                gm.reset()

