# coding=utf-8
"""
  名称:长度换算
  作者:万星明
  时间:2019/5/12 22:38
  注释:英制单位英寸和公制单位厘米互换
"""

value = float(input("请输入长度:"))
unit = input("请输入单位:")

if unit == "in" or unit == "英寸":
    print("%f英寸 = %f厘米" % (value, value * 2.54))
elif unit == "cm" or unit == "厘米":
    print("%f厘米 = %f英寸" % (value, value / 2.54))
else:
    print("请输入有效单位！")
