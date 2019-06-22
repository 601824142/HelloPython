# coding=utf-8
"""
   作者:万星明
   类名:
   注释:跑马灯效果招牌
   日期:2019/6/22 11:14
"""

import os
import time


def main():
    abc = '欢迎来到召唤师峡谷!'
    while True:
        print(abc)
        time.sleep(0.2)
        abc = abc[1:] + abc[0:1]
        # 调用系统命令
        os.system('cls')


if __name__ == '__main__':
    main()
