import random
import math
import numpy as np


def random_pick(some_list, probabilities):
    """
    :param some_list: 属性列表
    :param probabilities: 对应的属性概率
    :return: 选择结果
    """
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(some_list, probabilities):
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item


def exponentSelectB(A, elist, epsilon, n):
    """
    ******** exponentSelectA函数用来实现首节点的抽样
    计算首节点选择的指数机制
    :param A: 属性列表
    :param elist: 属性评分
    :return:
    """
    SelectR = 0
    exponent_list = []
    for i in range(len(elist)):
        exponent_list.append(np.exp((elist[i] * epsilon) / ((len(A) - 1) * (6 / n + 4 / (n**2)))))
    exponent_sumlist = []
    exponent_sum = sum(exponent_list)
    for j in range(len(elist)):
        exponent_sumlist.append(exponent_list[j]/exponent_sum)
        SelectR = random_pick(A, exponent_sumlist)
    return SelectR


def exponentSelectA(le, elist, indexlist, epsilon1, k, n):
    """
    ******** exponentSelectA函数用来实现AP对的抽样
    :param le: 属性个数
    :param elist: 评分矩阵
    :param indexlist: AP对矩阵 对应评分矩阵
    :param epsilon:  隐私预算
    :param k:  首节点个数
    :param n:  元组个数
    :return:
    """
    a = 0
    b = 0
    exponent_list1 = []

    exponent_sum = 0
    for i in range(len(elist)):
        exponent_list1t = []
        if len(indexlist[i]) == 1:
            exponent_list1t.append(0)
        else:
            for j in range(len(elist[i])):
                exponent_list1t.append(math.exp((0.1 * elist[i][j] * epsilon1 * 0.7 / (le - k)) / (6 / n + 4 / (n ** 2))))
        exponent_list1.append(exponent_list1t)  # exponent_list1为新的评分表
    print(exponent_list1)
    for ii1 in exponent_list1:
        for ii2 in ii1:
            exponent_sum += ii2
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for ii in range(len(elist)):
        for ji in range(len(elist[ii])):
            exponent_list1[ii][ji] = exponent_list1[ii][ji] / exponent_sum
    print(exponent_list1)
    for k1 in range(len(elist)):
        for k2 in range(len(elist[k1])):
            cumulative_probability += exponent_list1[k1][k2]
            if x < cumulative_probability:
                a = indexlist[k1][0]
                b = indexlist[k1][k2+1]
                print('ab==========================================')
                print(a)
                print(b)
                return a, b


def exponentSelectV(elist, indexlist):  # warning：此处返回值可能有错！！！！！！！！！！！！！！！！！！！！！！！！
    """
    ******** exponentSelectV函数用来抽样首节点
    :param le: 属性个数
    :param elist: 评分矩阵
    :param indexlist: AP对矩阵 对应评分矩阵
    :param epsilon:  隐私预算
    :param k:  首节点个数
    :param n:  元组个数
    :return:
    """
   # print('----------------')
    print('elist+++++++++++++++++++++++++++++++++++++++++')

    print(elist)

    print('indexlist')

    print(indexlist)
    x = random.uniform(0, 1)
    print('随机数为')
    print(x)
    cumulative_probability = 0.0
    for k1 in range(len(elist)):
        cumulative_probability += elist[k1]
        if x < cumulative_probability:
            return indexlist[k1]  # 原因：可能存在不满足上if的情况 一定是这里返回了null
    print('确定没有返回值！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！')
    sumK2 = 1 / len(elist)
    print('有继续运行')
    cumulative_probability1 = 0
    for k2 in range(len(elist)):
        cumulative_probability1 += sumK2
        if x < cumulative_probability1:
            return indexlist[k2]



















