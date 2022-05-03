# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 18:16
# @Author  : qixuejian
# @FileName: ScoreCalculator.py
# @Software: PyCharm
import math


def CalScore(nplist, le, n):
    """

    :param list1: 数据集
    :return: 评分矩阵
    """
    # 计算评分
    """
    最后修改时间：2020.06.02.18:11
    此模块功能为对数据集两两属性间评分矩阵的计算
    调用CalScore函数可以返回上述评分列表
    此处设置了3种评分函数：I，R，F（F评分未实现）
    """

    ScoreMatrix = [[0] * le for s1 in range(le)]  # 评分矩阵
    Node = 0  # 当前节点序号
    while Node < le - 1:
        print(Node)
        Node1 = 0
        while Node1 < le:
            if Node1 > Node:
                print("node", Node1)
                Fir = []  # 参与计算的第一个属性
                Sec = []  # 参与计算的第二个属性
                Res = []  # 保存结果 为矩阵 此处应有大小设置待写
                Fir = list(nplist[:, Node])  # 获取node列列表
                Sec = list(nplist[:, Node1])
                fir = set(Fir)
                sec = set(Sec)
                PrMatrix = [[0] * len(fir) for s1 in range(len(sec))]
                hf = 0
                for elem1 in fir:  # 第一个属性
                    hs = 0
                    for elem2 in sec:  # 第二个属性
                        s = 0
                        count1 = 0
                        while s < n:
                            if Fir[s] == elem1 and Sec[s] == elem2:
                                count1 += 1
                            s += 1
                        PrMatrix[hs][hf] = count1
                        hs += 1
                    hf += 1
                w1 = 0
                t1 = [0]*len(sec)
                while w1 < len(sec):   # 第二个属性概率分布由t1表示
                    w2 = 0
                    while w2 < len(fir):
                        t1[w1] += PrMatrix[w1][w2]
                        w2 += 1
                    w1 += 1
                ss2 = 0
                t2 = [0]*len(fir)   # 第一个属性概率分布由t2表示
                while ss2 < len(fir):
                    ss1 = 0
                    while ss1 < len(sec):
                        t2[ss2] += PrMatrix[ss1][ss2]
                        ss1 += 1
                    ss2 += 1
                ww1 = 0  # ww1 表示第二个属性分布下标
                mi1 = 0
                while ww1 < len(sec):
                    ww2 = 0   # ww2 表示c属性分布下标
                    while ww2 < len(fir):
                        # if t1[ww1] == 0 or t2[ww2] == 0 or PrMatrix[ww1][ww2] == 0:
                         #   mit = 0
                        # else:
                            # 互信息：
                            # mit = (float(PrMatrix[ww1][ww2])/38000.0) * math.log((PrMatrix[ww1][ww2])/(t1[ww1]*t2[ww2]/38000),2)
                            # F函数：
                            # R函数：
                        mit = abs(PrMatrix[ww1][ww2]/38000-t1[ww1]*t2[ww2]/(38000*38000)) * 0.5
                        mi1 += mit
                        ww2 += 1
                    ww1 += 1
                mi1 = round(mi1, 6)
                ScoreMatrix[Node][Node1] = mi1
                ScoreMatrix[Node1][Node] = mi1
                Node1 += 1
            else:
                Node1 += 1
        Node += 1
    # print(ScoreMatrix)
    return ScoreMatrix

