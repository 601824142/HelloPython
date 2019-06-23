# coding=utf-8
"""
  名称:二进制文件流
  作者:万星明
  时间:2019/6/23 15:16
  注释:
"""


def main():
    try:
        with open('sources/wo.jpg', 'rb') as file1:
            data = file1.read()
            print(type(file1.read()))
        with open('sources/data.png', 'wb') as file2:
            file2.write(data)

    except FileNotFoundError as e:
        print("指定文件无法打开:" + e)
    except IOError as e:
        print("读写文件出现错误:" + e)
    print("程序执行完毕!")


if __name__ == '__main__':
    main()
