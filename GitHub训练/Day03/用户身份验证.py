# coding=utf-8
"""
  名称:用户身份验证
  作者:万星明
  时间:2019/5/12 23:18
  注释:用户身份验证
"""
import getpass

username = input("请输入用户名:")
# password = input("请输入密码:")
password = getpass.getpass("请输入密码:")

if username == "admin" and password == "admin":
    print("身份验证成功！")
else:
    print("身份验证失败！")