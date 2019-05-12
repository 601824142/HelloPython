# coding=utf-8
"""
  名称:百分制成绩转换
  作者:万星明
  时间:2019/5/12 22:44
  注释:百分制成绩转等级制成绩
"""

score = float(input("请输入成绩:"))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"

print("你的等级是:"+grade)
