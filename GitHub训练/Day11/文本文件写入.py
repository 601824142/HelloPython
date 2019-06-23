# coding=utf-8
"""
  名称:文本文件写入
  作者:万星明
  时间:2019/6/22 22:49
  注释:
"""
from math import sqrt


def is_prime(n):
    """判断是否是素数"""
    # 断言n大于0
    assert n > 0
    # 从2到开根号n加1
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('sources/100.txt', 'sources/1000.txt', 'sources/10000.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as error:
        print("写入文件IO错误:%s" % error)
    finally:
        for fs in fs_list:
            fs.close()
        print("文件写入成功!")



if __name__ == '__main__':
    main()