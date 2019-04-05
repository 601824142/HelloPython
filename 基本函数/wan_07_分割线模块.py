def test1():
    """打印分隔线"""
    print("*" * 10)


def test2(char):
    """自定义字符打印分隔线"""
    print(char * 10)


def test3(char, times):
    """自定义字符次数打印分隔线"""
    print(char * times)


def test4(char, times):
    """打印5行分隔线
    :param char: 分隔线使用的字符
    :param times:字符打印次数
    """
    row = 0
    while row < 5:
        test3(char, times)
        row += 1


name = "万星明"
