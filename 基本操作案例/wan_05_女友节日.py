# 定义节日字符串变量记录节日名称
holidayName = input("请输入节日名称:")

# 如果是情人节,应该买玫瑰花/看电影
if holidayName == "情人节":
    print("买玫瑰")
    print("看电影")
# 如果是平安夜,应该买苹果/吃大餐
elif holidayName == "平安夜":
    print("买苹果")
    print("吃大餐")
# 如果是其他的,就打炮
else:
    print("打炮")
