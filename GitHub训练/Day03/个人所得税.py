# coding=utf-8
"""
  名称:个人所得税
  作者:万星明
  时间:2019/5/12 23:01
  注释:输入月收入和五险一金计算个人所得税(旧版算法)
"""

salary = float(input("本月收入:"))
insurance = float(input("五险一金:"))
taxAmount = salary - insurance - 3500
if taxAmount <= 0:
    taxRate = 0
    taxTotal = 0
elif taxAmount < 1500:
    taxRate = 0.03
    taxTotal = 0
elif taxAmount < 4500:
    taxRate = 0.1
    taxTotal = 105
elif taxAmount < 9000:
    taxRate = 0.2
    taxTotal = 555
elif taxAmount < 35000:
    taxRate = 0.25
    taxTotal = 1005
elif taxAmount < 55000:
    taxRate = 0.3
    taxTotal = 2755
elif taxAmount < 80000:
    taxRate = 0.35
    taxTotal = 5505
else:
    taxRate = 0.45
    taxTotal = 13505

tax = abs(taxAmount * taxRate - taxTotal)
print("个人所得税:%.2f元" % tax)
print("实际到手：%.2f元" % (taxAmount + 3500 - tax))
