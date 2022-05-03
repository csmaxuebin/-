# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 15:56
# @Author  : qixuejian
# @FileName: ProDist.py
# @Software: PyCharm
import numpy as np
from LaplaceNoice import add_lapnoice
from itertools import product as pr


def GetFNProDist(lis, FNode, n, npLis, epsilon, sensitivity):
    """
    得到首节点分布的函数
    :param FNode: 首节点
    :param n: 元组个数
    :param npLis: np数据集
    :param epsilon: 隐私预算
    :param sensitivity: 敏感度
    :return:
    """
    print('进入函数体内部')
    print('Fnode')
    print(FNode)
    temps = []
    JMaxlis = []

        # JMax = np.hstack(JMax, npLis[i])  # ！！！！！！！！！！！！！！！！！！！！！hstack需要改

    print(FNode[0])
        # 结果可以执行到这里
    for nq in range(n):
        Jt1 = []
        for i in range(len(FNode)):

            Jt1.append(lis[nq][FNode[i]])
        JMaxlis.append(Jt1)
    print("jmax")
    print(JMaxlis)
    # for nq in range(n):
    #     JMaxt = []
    #     for i in FNode:
    #         JMaxt.append(lis[nq][i])
    #     JMaxlis.append(JMaxt)  # JMaxlis是首节点数据集
    JMax = np.array(JMaxlis)
    # print(JMax)
    #        此处出问题
    print(len(FNode))
    for iv in range(len(FNode)):
        print('22222222')
        print(iv)

        temps.append(set(JMax[:, iv]))
    print('temps')
    print(temps)
    # JMax = list(JMax)

    J4 = []
    for ss in pr(* temps):
        J4.append(list(ss))  # j4 为所有可能取值列表
    print('J4')
    print(J4)
    Plist = [0] * len(J4)
    js = 0
    while js < len(J4):  # Plist中存储了首节点的联合分布 与J4下标对应
        for n1 in range(n):
            if JMaxlis[n1] == J4[js]:
                Plist[js] += 1

        Plist[js] = Plist[js] / n
        Plist[js] += add_lapnoice(epsilon, sensitivity)  # 对首节点原始分布进行加噪
        js += 1

    for jis in range(len(Plist)):
        if Plist[jis] < 0:
            Plist[jis] = 0
    sumPlist = sum(Plist)
    for jis1 in range(len(Plist)):
        Plist[jis1] = Plist[jis1] /sumPlist
    print('Plist')
    print(Plist)
    print('到返回前 ')
    return Plist, J4


def GetKProDist(FNode1, Kid, n, npLis, lis, epsilon, sensitivity):
    """
    得到Ap对的联合分布
    :param FNode1: 父节点
    :param Kid: 子节点
    :param n: 元组个数
    :param npLis: np数据集
    :param epsilon: 隐私预算
    :param sensitivity: 敏感度
    :return: 返回分布列表 和对应的具体值
    """
    JMax1 = []
    # temps1 = [set(npLis[:, Kid])]
    temps1 = []
    kii = set(npLis[:, Kid])
    temps1.append(kii)  # temps1 带子节点的集合

    temp2 = []  # temp2 不带子节点
    for i in FNode1:
        # JMax1 = np.hstack(JMax1, npLis[i])  # ！！！！！！！！！！！！！！！！！！！！！hstack需要改
        temps1.append(set(npLis[:, i]))
        temp2.append(set(npLis[:, i]))

    for i12 in range(n):
        t11 = [lis[i12][Kid]]
        for i13 in FNode1:
            t11.append(lis[i12][i13])
        JMax1.append(t11)

    Jk3 = []  # Jk3 为父节点属性对应值 后面用到
    for si in pr(* temp2):
        Jk3.append(list(si))

    Jk4 = []
    for ss in pr(* temps1):
        Jk4.append(list(ss))
    Plistk = [0] * len(Jk4)

    jsp = 0
    for js1 in Jk4:  # Plist中存储了首节点的联合分布 与Jk4下标对应
        for n1 in range(n):
            if JMax1[n1] == js1:
                Plistk[jsp] += 1
        Plistk[jsp] = Plistk[jsp] / n
        Plistk[jsp] += add_lapnoice(epsilon, sensitivity)  # 对首节点原始分布进行加噪
        jsp += 1
    for jq in range(len(Plistk)):
        if Plistk[jq] < 0:
            Plistk[jq] = 0
    sumPlistk = sum(Plistk)
    for jq1 in range(len(Plistk)):
        Plistk[jq1] = Plistk[jq1] /sumPlistk
    print('Plistk')
    print(Plistk)
    print('Jk4')
    print(Jk4)
    print('Jk3')
    print(Jk3)
    print('kii')
    print(kii)
    return Plistk, Jk4, Jk3, kii


"""
    以下计算条件概率
"""


def GetCProDist(Plistk, Jk4, Jk3, Kii):  # warning：此处子节点属性貌似多了一个null 由Kii传入
    """
    在联合概率下计算条件概率
    :param Plistk: 概率列表
    :param Jk4: 概率列表对应的取值
    :return:
    """

    Kii = list(Kii)
    Cpro1 = []  # 父节点为i时的全部条件概率分布
    for i in Jk3:  # Jk3 为父节点属性对应值
        CPro = [0] * len(Kii)  # 当父节点为i时的子节点条件概率分布
        Pb = 0
        Pab = [0] * len(Kii)
        for ij in range(len(Jk4)):
            if Jk4[ij][1:] == i:
                Pb += Plistk[ij]
                for j in range(len(Kii)):
                    if Jk4[ij][0] == Kii[j]:
                        Pab[j] += Plistk[ij]  # CPro[j]为子节点是kii中

        for joo in range(len(Kii)):
            if Pb != 0:
                CPro[joo] = Pab[joo] / Pb
        Cpro1.append(CPro)
    return Cpro1

    # Cpro1 = []  # 父节点为i时的全部条件概率分布
    # for i in Jk3:# Jk3 为父节点属性对应值
    #     CPro = [0] * len(Kii)  # 当父节点为i时的子节点条件概率分布
    #     for j in Kii:  # kii  子节点取值
    #         num = 0
    #         Pab = 0
    #         Pb = 0
    #         Palb = 0
    #         for ij in range(len(Jk4)):
    #             print('Jk4[ij][1:]')
    #             print(Jk4[ij][1:])
    #             print('=====')
    #             print(j)
    #             if Jk4[ij][1:] == j:
    #                 Pb += Plistk[ij]
    #                 if Jk4[ij][0] == Kii:
    #                     Pab = Plistk[ij]
    #         print(Pb)
    #         if Pb != 0:
    #             Palb = Pab / Pb
    #             print('Palb')
    #         CPro[num] = Palb   # CPro[num]表示子节点值为j时的条件概率分布
    #     Cpro1.append(CPro)
    # return Cpro1


def GetIsoProDist(isolist ,nplis,blis, n, epsilon, sensitivity):
    pro = []  # pro 是概率
    pros = []  # pros 是属性
    for i in isolist:
        print('-----------------------------------------------------')
        print(i)
        prost = []
        a = []
        ib = 0
        while ib < n:
            print(ib)
            print('ib的类型')
            print(type(ib))
            print(type(a))
            print(blis[ib][i])
            print(type(blis[ib][i]))
            a.append(blis[ib][i])
            ib += 1
        #  a = list(nplis[:, i])  # a是数据集
        print('a')
        print(a)
        # print('seta')
        # print(set(a))
        print(type(a))
        prot = []

        #      b = list(set(a))

        b = list(set(a))
        prost = b
        for att in b:
            cout = 0
            for num in range(n):
                if a[num] == att:
                    cout += (1 / n)
            prot.append(cout + add_lapnoice(epsilon, sensitivity))

    #     print('prot')
    #     print(prot)
    # 1/0
        for nu1 in range(len(prot)):
            if prot[nu1] < 0:
                prot[nu1] = 0
        protnum = sum(prot)
        for nu11 in range(len(prot)):
            prot[nu11] = prot[nu11] / protnum
        pro.append(prot)
        pros.append(prost)
    return pro, pros
























