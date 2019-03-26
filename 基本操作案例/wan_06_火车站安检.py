# 定义布尔型变量hasTicket表示是否有车票
hasTicket = bool(input("是否有车票:"))
# 定义整型变量knifeLength表示刀的长度,单位：厘米
knifeLength = int(input("刀的长度:"))
# 首先检查是否有车票,如果有,才允许进行安检
if hasTicket:
    print("已验证车票,正在安检！")
    # 安检时,需要检查刀的长度,判断是否超过20CM
    if knifeLength > 20:
        # 如果超过20CM,提示刀的长度,不允许上车
        print("刀具长度超过20,请下车！")
    else:
        # 如果不超过20CM,安检通过
        print("安检通过,请上车！")
# 如果没有车票，不允许进站
else:
    print("请先买票！")
