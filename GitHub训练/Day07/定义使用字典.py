# coding=utf-8
"""
  名称:定义使用字典
  作者:万星明
  时间:2019/6/21 19:36
  注释:
"""


def main():
    scores = {'万星明': 90, '朱秀娟': 80, '万星月': 95}
    print(scores['万星明'])
    print(scores['万星月'])

    for elem in scores:
        print('%s\t---->\t%d' % (elem, scores[elem]))
    scores['万星明'] = 100
    scores['朱秀娟'] = 90
    scores.update(万玉琴=60, 朱秀媛=78)

    print(scores)
    if '朱正' in scores:
        print(scores['朱正'])

    print(scores.get('朱正'))
    print(scores.get('朱正', 55))
    print(scores.popitem())
    print(scores.pop('万星明', 120))

    scores.clear()

    print(scores)


if __name__ == '__main__':
    main()
