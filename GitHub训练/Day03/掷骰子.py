# coding=utf-8
"""
  名称:掷骰子
  作者:万星明
  时间:2019/5/12 22:55
  注释:掷骰子决定做什么事情
"""

from random import randint

face = randint(1, 6)
if face == 1:
    result = "唱歌"
elif face == 2:
    result = "跳舞"
elif face == 3:
    result = "狗叫"
elif face == 4:
    result = "俯卧撑"
elif face == 5:
    result = "绕口令"
else:
    result = "讲笑话"

print("骰子为:%d,你需要%s" % (face, result))
