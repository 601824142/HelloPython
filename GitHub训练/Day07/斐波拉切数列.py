# coding=utf-8
"""
   作者:万星明
   类名:
   注释:生成斐波拉切数列
   日期:2019/6/22 10:18
"""


def main():
    f = [1, 1]
    for i in range(2, 20):
        f += [f[i - 1] + f[i - 2]]
        # f.append(f[i - 1] + f[i - 2])
    for val in f:
        print(val, end=' ')


def test():
    wan = [1, 2, 3]
    wan += [wan[2] + 1]
    print(wan)


if __name__ == '__main__':
    test()
