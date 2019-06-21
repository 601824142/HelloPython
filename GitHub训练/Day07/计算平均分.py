# coding=utf-8
"""
  名称:计算平均分
  作者:万星明
  时间:2019/6/21 19:31
  注释:
"""

def main():
    number = int(input('请输入学生人数: '))
    names = [None] * number
    scores = [None] * number
    for index in range(len(names)):
        names[index] = input('请输入第%d个学生的名字: ' % (index + 1))
        scores[index] = float(input('请输入第%d个学生的成绩: ' % (index + 1)))
    total = 0
    for index in range(len(names)):
        print('%s: %.1f分' % (names[index], scores[index]))
        total += scores[index]
    print('平均成绩是: %.1f分' % (total / number))


if __name__ == '__main__':
    main()