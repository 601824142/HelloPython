# 导包
import random

# 从控制台输入要出的拳 ——石头(1)/剪刀(2)/布(3)
player = int(input("请输入您出的拳(石头(1)/剪刀(2)/布(3)):"))

# 电脑随机出拳——先假定电脑只会出石头
computer = random.randint(1, 3)
print("玩家出的拳头是:%d VS 电脑出的拳头是:%d" % (player, computer))

# 比较胜负
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("你赢了！")
elif player == computer:
    print("平局！")
else:
    print("电脑赢了！")
