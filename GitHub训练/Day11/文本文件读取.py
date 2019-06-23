# coding=utf-8
"""
  名称:文本文件读写
  作者:万星明
  时间:2019/6/22 21:58
  注释:
"""

# 直接读取文件
import time


def test01():
    # file = open("D:/Python/WorkSpace/HelloPython/GitHub训练/Day11/sources/文件流读取.txt", 'r', encoding='gbk')
    file = open("sources/文件流读取.txt", 'r', encoding='gbk')
    print(file.read())
    file.close()


# 读取并抛出异常
def test02():
    file = None
    try:
        file = open("sources/文件流读取.txt", 'r', encoding='utf-8')
        print(file.read())
    except FileExistsError:
        print("文件不存在!")
    except FileNotFoundError:
        print("无法打开指定文件!")
    except LookupError:
        print("指定了未知编码!")
    except UnicodeDecodeError:
        print("读取文件指定编码错误！")
    finally:
        if file:
            file.close()


# 指定文件上下文对象,在离开时自动释放资源
def test03():
    try:
        with open("sources/文件流读取.txt", 'r', encoding='utf-8') as file:
            print(file.read())
    except FileExistsError:
        print("文件不存在!")
    except FileNotFoundError:
        print("无法打开指定文件!")
    except LookupError:
        print("指定了未知编码!")
    except UnicodeDecodeError:
        print("读取文件指定编码错误！")


# 逐行读取或读取到列表容器
def test04():
    # 一次性读取
    with open("sources/文件流读取.txt", 'r', encoding='gbk') as file:
        print(file.read())

    # 通过for-in逐行读取
    with open("sources/文件流读取.txt", mode='r') as file:
        for line in file:
            print(line, end=' ')
            time.sleep(0.5)
    print()

    # 按行读取文件到列表中
    with open("sources/文件流读取.txt") as file:
        lines = file.readlines()
    print(lines[2])


# 判断圆周率是否包含生日
def test05():
    birth = input("请输入你的生日:")
    with open('sources/圆周率.txt') as file:
        lines = file.readline()
        pi_str = ''
        for line in lines:
            pi_str += line.strip()
            print(">>>"+pi_str)
        if birth in pi_str:
            print("你的生日包含在圆周率中!")


if __name__ == '__main__':
    test05()
