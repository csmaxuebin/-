# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 10:53
# @Author  : qixuejian
# @FileName: FNZ.py
# @Software: PyCharm

# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/5 17:00
# @Author  : qixuejian
# @FileName: FirstNode.py
# @Software: PyCharm
import numpy as np
from ExponentMachine import exponentSelectB
import random
import math


def selectFNZ(npda, epsilon1, theta, n, A, le, epsilon2):
    """

    :param tli: 评分矩阵
    :param npda: np数据集
    :param epsilon: 隐私预算
    :param theta: 信噪比
    :param n: 元组个数
    :param l: 属性个数
    :return: 返回父节点个数以及父节点集
    """
    Ks = 1
    for k in range(len(A)):
        thetaK = (epsilon2 * n) / ((2 ** (Ks + 1)) * (le - Ks))  # 计算当前个节点的信噪比
        if thetaK < theta:
            break
        Ks += 1
    F1 = [a1 for a1 in range(le)]
    FN = math.floor(random.uniform(0, le + 1))
    # tlis = np.array(tli)
    # Ssum = tlis.sum(axis=1)
    # Slist = list(Ssum)
    # FN = []
    # num = 1
    # Ks = 1
    # for k in range(len(tli)):
    #     tempindex = exponentSelectB(A, Slist, epsilon1, n)  # 获得最大值索引
    #     Slist[tempindex] = 0  # 将当前最大值改为0，目的是后面不再取到这个值
    #     # num = num * len(set(npda[:, tempindex]))  # 求此属性的取值个数
    #     thetaK = (epsilon2 * n) / ((2 ** (Ks + 1)) * (le - Ks))  # 计算当前个节点的信噪比
    #     if thetaK < theta:
    #         break
    #     FN.append(tempindex)  # 将选出节点放入列表
    #     Ks += 1

    return FN, Ks - 2


