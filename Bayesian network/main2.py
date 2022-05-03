# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/17 1:19
# @Author  : qixuejian
# @FileName: main2.py
# @Software: PyCharm
import time
import numpy as np
import gc
from ScoreCalculator import CalScore
from FirstNode import selectFN
from BayesianNet import GetNet
from ProDist import GetFNProDist, GetKProDist, GetCProDist, GetIsoProDist
from ExponentMachine import exponentSelectV


stime = time.process_time()
f = open('acs.data', 'r')
a = f.read()
f.close()
b = eval(a)
n = len(b)
le = len(b[0])
c = np.array(b)
A = [a1 for a1 in range(le)] # A 为节点列表
epsilon = 1.6    # 隐私预算37开 网络阶段3 分布7
"""
1.网络阶段隐私预算： 首节点分配30% 其余均分70%  -- 即首节点分配 0.3X0.3=0.09  --其余分布分配 0.21 / d-k
2.分布阶段隐私预算：一共d-k+1个分布均分  -- 即每个分布分配 0.7 / d-k+1
"""
epsilon1 = 0.3 * epsilon
epsilon2 = 0.7 * epsilon

theta = 4


netP = [[9, 19, 12, 20, 13],[9, 19, 13, 18, 15],[9, 12, 20, 13, 18],[19, 12, 20, 13, 18],[19, 13, 18, 15, 10],[9, 19, 18, 15, 0],[20, 13, 18, 15, 11],
        [9, 20, 13, 15, 1],[9, 15, 10, 5, 1],[9, 20, 13, 11, 6],[18, 15, 0, 5, 3],[12, 18, 11, 0, 2],[9, 12, 11, 10, 2],[19, 12, 20, 6, 7],[9, 13, 1, 3, 14]
        ,[19, 13, 7, 14, 8],[9, 18, 11, 1, 21]  ]
netK = [15,11,4,10,0,5,1,3,6,7,2,22,16,14,8,21,17]
ISO = []
FNode = [9, 19, 12, 20, 13, 18]
K = 5

# 得到噪化的概率分布
"""
Firstnode:[7, 6, 5, 13, 14, 12, 8, 11]
[7, 6, 13, 14, 12, 8, 11] -------------> 3
[7, 6, 5, 13, 12, 11, 3] -------------> 10
[7, 6, 5, 13, 14, 11, 3] -------------> 1
[7, 6, 13, 8, 3, 10, 1] -------------> 4
[6, 14, 12, 8, 11, 3, 4] -------------> 0
[6, 13, 14, 12, 8, 10, 0] -------------> 15
[13, 12, 11, 1, 4, 0, 15] -------------> 9
[7, 6, 5, 14, 10, 1, 15] -------------> 2
"""
print('已经构成网络')



"""
以上为构造贝叶斯网络
以下为计算概率分布
"""

FPro, Alist = GetFNProDist(b, FNode, n, c, epsilon2 / (le - 7), 2 / n)  # 敏感度待分配
print('已经完成首节点概率计算')
#  需要生成概率分布并加入噪声
FkP = []  # 存储分布
FKL = []  # 存储FkP对应属性
CPR = []
JK33 = []
KII = []
for jf in range(len(netK)):  # 得到了分布列表FkP和对应值列表FKL
    print(jf)
    FKPro, FKlist, Jk3, Kii = GetKProDist(netP[jf], netK[jf], n, c, b, epsilon2 / (le - 7), 2 / n)   # 敏感度待分配
    Cpro = GetCProDist(FKPro, FKlist, Jk3, Kii)   # 获得条件分布
    KII.append(list(Kii))
    FkP.append(FKPro)
    FKL.append(FKlist)
    CPR.append(Cpro)
    JK33.append(Jk3)
Isopro = 0
Isopros = 0
if ISO != 0:
    print('ISO')
    print(ISO)
    Isopro, Isopros = GetIsoProDist(ISO, c, b, n, epsilon2 / (le - 7), 2 / n)

# 得到贝叶斯网络后使用网络得到合成数据集
"""
1. 首先生成每个元组的首节点属性值
2. 接着根据netP与netK列表生成后面的属性值
3.可以直接放到一个列表中，不用输出文件
"""
synlist = []
for nnn in range(n):
    synS = [0] * le  # 存储单个元组
    outF = exponentSelectV(FPro, Alist)
    iss = 0
    for af1 in FNode:  # 第7个属性出问题
        synS[af1] = outF[iss]
        iss += 1
    """
    上面循环实现了将首节点放入synS
    下面需要将子节点放入synS
    """
    kss = 0
    for ak in netK:
        print('****************')
        print(ak)
        fss = netP[kss]  # fss 为父节点
        fflist = []
        for nod1 in fss:  # 取得父节点的值
            fflist.append(synS[nod1])
        print()
        # CPR[kss]为当前子节点的
        for nums in range(len(JK33[kss])):
            if fflist == JK33[kss][nums]:  # JK33[kss][nums]是父节点值，CPR[kss][nums]为对应条件概率
                synS[ak] = exponentSelectV(CPR[kss][nums], KII[kss])
        # if synS[ak] == None:
        #     1 / 0
        kss += 1

    for bk in range(len(Isopros)):
        outS = exponentSelectV(Isopro[bk], Isopros[bk])
        synS[ISO[bk]] = outS


    synlist.append(synS)
for iqq in synlist:
    print(iqq)
f = open('acs_0.2_syn.data', 'w')
f.write(str(synlist))
f.close()


etime = time.process_time()
print('Running time: %s Seconds' % (etime-stime))

