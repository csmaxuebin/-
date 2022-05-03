# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 11:09
# @Author  : qixuejian
# @FileName: BNZ.py
# @Software: PyCharm

# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/6 21:05
# @Author  : qixuejian
# @FileName: BayesianNet.py
# @Software: PyCharm
import itertools
import numpy as np
from ExponentMachine import exponentSelectA, exponentSelectB
from itertools import product as pr


def GetKids(A, Fset):
    """
    :param A: 属性
    :param Fset: 父节点集
    :return: 返回子节点集
    """
    c = []
    for i in A:
        if i not in Fset:
            c.append(i)
    return c


def GetNet(lis, npLis, A, FNode, epsilon1, theta, n, K, le, epsilon2):
    """
    :param npLis:非np数据集
    :param A: 所有属性
    :param K: 首节点个数
    :param FNode: 首节点
    :param epsilon: 隐私预算
    :param theta: 信噪比
    :param n: 元组个数
    :return: Ftot[Y][0], Ftot[Y][X] 返回选出的父子节点
    """
    Fset = FNode  # 得到了父节点候选集
    Kset = GetKids(A, Fset)  # 得到子候选集
    Fs = []
    Fs1 = [0]
    Fst = []  # 用来存储子节点与该子节点的父节点集
    Ftot = []  # 用来存储所有Fst
    Stot = []
    # 对父候选集进行筛选 以及计算信噪比 删除子集 得到P的集合
    # if len(Fset) + 1 < 6:
    #     maxlen = len(Fset) + 1
    # else:
    #     maxlen = 5
    # for ii in range(1, maxlen):  # 得到全部候选的父节点集
    iter1 = itertools.combinations(Fset, K)
    for i in iter1:
            # print('listi')
            # print(list(i))
        Fs.append(list(i))
    # print('kset:')
    # print(Kset)
    # print('Fs:')
    # print(Fs)
    # fsf = []
    # for i5 in Fs:
    #     for i7 in i5:
    #         fsf.append(i7)
    # print('fsf')
    # print(fsf)

    for s in Kset:  # 计算满足子节点为s 时 信噪比的父节点集
        Fs1 = []
        Fs1.append(s)
        for ss in Fs:  # ss为父节点集
            # product = len(set(npLis[:, s]))
            # for it1 in ss:
            #     # print('it1')
            #     # print(it1)
            #     # print('------product')
            #     # print(product)
            #     # print('len(set(npLis[:, it1]))')
            #     # print(len(set(npLis[:, it1])))
            #     product *= len(set(npLis[:, it1]))
            # if (epsilon2 * n) / (product * (le - K + 1)) > theta:
            Fs1.append(ss)  # Fs1里面存的是满足信噪比的父节点  # ++++++++++++++++ 以上过 ++++++++++++++++++++++++
        # Fs2 = []
        # Fs3 = []
        # for j in range(1, len(Fs1)):  # 删除s中的子集
        #     for jj in range(1, len(Fs1)):
        #         if Fs1[j] != Fs1[jj] and set(Fs1[j]).issubset(Fs1[jj]):
        #             Fs2.append(Fs1[j])  # 此后Fs1里面不存在子集
        # for ite in Fs1:
        #     if ite not in Fs2:
        #         Fs3.append(ite)
        # Ftot.append(Fs3)   # Fs3 存储的是全部用来计算评分函数的父节点集
        Ftot.append(Fs1)
    # print('Ftot:')
    # print(Ftot)

    # Stot = []
    # for nii in range(len(Ftot)):
    #     stotp = []
    #     for mii in range(len(Ftot[nii])):
    #         stotp.append(0)
    #     Stot.append(stotp)

    # 每一个AP对进行评分，得到评分列表

    for yi in range(len(Ftot)):  # yi为取出每个子节点
        Stotx = []
        for xi in range(1, len(Ftot[yi])):  # xi为取出每个子节点的父节点集
            #for zi in Ftot[yi][xi]:  # zi是一个父节点集中的节点
            # t = np.hstack(t, npLis[zi]) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!hstack 需要改 ***已修改
            t = []
            for n1a in range(n):
                ts = []
                for zi in Ftot[yi][xi]:
                    ts.append(lis[n1a][zi])
                t.append(ts)  # t为父节点组成的数据集列



            # if Ftot[yi][xi] == [3, 4]:
            #     print('t34')
            #     print(t)

            # t = np.delete(t, 0, axis=1)  # t是父节点np数据集
            kid1 = list(npLis[:, Ftot[yi][0]])
            kidset = set(kid1)  # 子节点拥有的属性集
            # numK = [[0] for nu1 in range(len(kidset))]

            # ********** 计算父节点属性种类***********************
            tus = []
            for iii in Ftot[yi][xi]:  # 一个父节点集
                tss = set(npLis[:, iii])   # 1111111111111111111111111111111
                tus.append(tss)               # **********************************以上过***************************************

            P2 = []
            for i in pr(* tus):
                P2.append(list(i))  # P2为所有可能的取值列表

            # if Ftot[yi][xi] == [3, 4]:
            #     print('p2')
            #     print(P2)

            # for nn in range(n):
            #     t1[nn] = str(t1[nn])
            # P2 = set(t1)
            # numP = [[0] for nu1 in range(len(P2))]
            """
            下循环计算 联合概率分布 ： numT
            """
            numT = [[0 for nu1 in range(len(P2))]] * len(kidset)
            kinum1 = 0
            for ki1 in kidset:  # 求得概率分布numT
                Panum1 = 0
                for temp11 in P2:
                    for ton in range(n):
                        if kid1[ton] == ki1 and t[ton] == temp11:  # P2
                            numT[kinum1][Panum1] += 1
                    Panum1 += 1
                kinum1 += 1


            # if Ftot[yi][xi] == [3, 4]:
            #     print('numt:')
            #     print(numT)


            """
            下循环计算 子节点边缘概率分布 ： kids
            """
            kids = [0 for i11 in range(len(kidset))]
            for kids1 in range(len(numT)):
                for kids2 in range(len(numT[0])):
                    kids[kids1] += numT[kids1][kids2]
            """
            下循环计算 父节点边缘概率分布 ： Pas
            """
            Pas = [0 for i11 in range(len(P2))]
            for Pas1 in range(len(P2)):
                for Pas2 in range(len(kidset)):
                    Pas[Pas1] += numT[Pas2][Pas1]

            Scores = 0
            for iny in range(len(numT)):
                for inx in range(len(numT[0])):
                    Scores += abs(numT[iny][inx] / 38000 - kids[iny] * Pas[inx] / (38000 * 38000)) * 0.5
            Stotx.append(Scores)
        Stot.append(Stotx)
    print('Ftot')
    print(Ftot)
    print('Stot')
    print(Stot)
    isotest = 0
    this_iso = []
    this_kid = 0
    this_Pa = 0
    for iso in Stot:
        for iso1 in iso:
            isotest += iso1
    if isotest == 0:
        for i in Ftot:
            this_iso.append(i[0])
        # this_iso = Ftot
    # 此处已经得到评分函数矩阵Stot 加噪指数机制抽样最大即可
    else:
        this_kid, this_Pa = exponentSelectA(len(A), Stot, Ftot, epsilon1, K, n)
    # print('kid')
    # print(this_kid)
    # print('pa')
    # print(this_Pa)
    # 得到Stot[yi][xi] 的坐标 对应找到Ftot = [] ftot[yi][0]存放的是子节点， ftot[yi][xi]存放的是父节点集合
    return this_kid, this_Pa, this_iso


def GetFKNet(lis, npLis, A, FNode, epsilon1, theta, n, K, le, epsilon2, KK):
    """
    :param npLis:非np数据集
    :param A: 所有属性
    :param K: 首节点个数
    :param FNode: 首节点
    :param epsilon: 隐私预算
    :param theta: 信噪比
    :param n: 元组个数
    :return: Ftot[Y][0], Ftot[Y][X] 返回选出的父子节点
    """
    Fset = FNode  # 得到了父节点候选集
    Kset = GetKids(A, Fset)  # 得到子候选集
    Ftot = []
    Stot = []
    for s in Kset:  # 计算满足子节点为s 时 信噪比的父节点集
        Ftot.append(s)

            # t = np.delete(t, 0, axis=1)  # t是父节点np数据集
        kid1 = list(npLis[:, s])
        kidset = set(kid1)  # 子节点拥有的属性集

        tus = []
        for iii in Fset:  # 一个父节点集
            tss = set(npLis[:, iii])   # 1111111111111111111111111111111
            tus.append(tss)               # **********************************以上过***************************************

        P2 = []
        for iw in pr(* tus):
            P2.append(list(iw))  # P2为所有可能的取值列表
        t = []
        for n in range(n):
            ts = []
            for zi in Fset:
                ts.append(lis[n][zi])
            t.append(ts)
            # if Ftot[yi][xi] == [3, 4]:
            #     print('p2')
            #     print(P2)

            # for nn in range(n):
            #     t1[nn] = str(t1[nn])
            # P2 = set(t1)
            # numP = [[0] for nu1 in range(len(P2))]
            """
            下循环计算 联合概率分布 ： numT
            """
        numT = [[0 for nu1 in range(len(P2))]] * len(kidset)
        kinum1 = 0
        for ki1 in kidset:  # 求得概率分布numT
            Panum1 = 0
            for temp11 in P2:
                for ton in range(n):
                    if kid1[ton] == ki1 and t[ton] == temp11:  # P2
                        numT[kinum1][Panum1] += 1
                Panum1 += 1
            kinum1 += 1


            # if Ftot[yi][xi] == [3, 4]:
            #     print('numt:')
            #     print(numT)


            """
            下循环计算 子节点边缘概率分布 ： kids
            """
        kids = [0 for i11 in range(len(kidset))]
        for kids1 in range(len(numT)):
            for kids2 in range(len(numT[0])):
                kids[kids1] += numT[kids1][kids2]
            """
            下循环计算 父节点边缘概率分布 ： Pas
            """
        Pas = [0 for i11 in range(len(P2))]
        for Pas1 in range(len(P2)):
            for Pas2 in range(len(kidset)):
                Pas[Pas1] += numT[Pas2][Pas1]

        Scores = 0
        for iny in range(len(numT)):
            for inx in range(len(numT[0])):
                Scores += abs(numT[iny][inx] / 38000 - kids[iny] * Pas[inx] / (38000 * 38000)) * 0.5
        Stot.append(Scores)

    this_kid = exponentSelectB(Ftot, Stot, epsilon1 / KK, n)
    return this_kid
