# coding=utf-8
"""
  名称:机器学习01
  作者:万星明
  时间:2019/6/23 23:07
  注释:
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def machine_study():
    """sklearn数据集学习"""

    # 获取数据集

    # print("鸢尾花数据集合:\n", iris)
    # print("查看数据集描述:\n", iris["DESCR"])
    # print("查看特征值名称:\n", iris.feature_names)
    # print("查看特征值:\n", iris.data, iris.data.shape)
    iris = load_iris()
    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)

    print("训练集特征值:\n", x_train, x_train.shape)
    return None


if __name__ == '__main__':
    machine_study()
