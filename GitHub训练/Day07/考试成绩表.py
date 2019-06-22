# coding=utf-8
"""
   作者:万星明
   类名:
   注释:学生考试成绩表
   日期:2019/6/22 11:22
"""
from random import randint


def main():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    subjects = ['语文', '数学', '英语']
    scores = [[0] * 3] * 5

    for row, name in enumerate(names):
        print('请输入%s的成绩' % name)
        scores[row] = [None] * len(subjects)
        for col, subj in enumerate(subjects):
            # score = float(input(subj + ': '))
            score = randint(1, 100)
            scores[row][col] = score
    print(scores)


if __name__ == '__main__':
    main()
