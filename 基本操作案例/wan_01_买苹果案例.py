# 1、输入苹果单价
# app_price = input("输入苹果单价：")
# 2、输入苹果购买重量
# app_weight = input("输入苹果重量：")
# 3、计算金额
# (1)将苹果单价转换成小数
price = float(input("输入苹果单价："))
# (2)将苹果的重量转换成小数
weight = float(input("输入苹果重量："))
# (3)计算付款金额
money = price * weight

print("苹果单价：%.02f元/斤,苹果重量：%.02f斤。共需要支付：%.02f元。" % (price, weight, money))
