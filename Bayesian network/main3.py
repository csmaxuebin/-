# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 16:03
# @Author  : qixuejian
# @FileName: main3.py
# @Software: PyCharm

import time
import numpy as np
import gc
from ScoreCalculator import CalScore
from FirstNode import selectFN
from BayesianNet import GetNet
from ProDist import GetFNProDist, GetKProDist, GetCProDist, GetIsoProDist
from ExponentMachine import exponentSelectV


stime = time.time()
f = open('nltcs.data', 'r')
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

# s = CalScore(c, le, n)  # s为评分矩阵
s = [[0, 0.132583, 0.138666, 0.130227, 0.12608, 0.136104, 0.13785, 0.1359, 0.129561, 0.130072, 0.122706, 0.127095, 0.126207, 0.122927, 0.122809, 0.123364], [0.132583, 0, 0.136742, 0.132259, 0.133457, 0.139635, 0.144094, 0.13827, 0.134079, 0.135737, 0.122706, 0.13448, 0.131666, 0.125851, 0.124441, 0.126234], [0.138666, 0.136742, 0, 0.138713, 0.130724, 0.147291, 0.141504, 0.136099, 0.12451, 0.13495, 0.122706, 0.12794, 0.122706, 0.122706, 0.122706, 0.12527], [0.130227, 0.132259, 0.138713, 0, 0.130011, 0.17541, 0.140778, 0.139217, 0.13595, 0.141595, 0.129701, 0.122706, 0.131605, 0.122809, 0.13014, 0.132785], [0.12608, 0.133457, 0.130724, 0.130011, 0, 0.135345, 0.139473, 0.137404, 0.137059, 0.132094, 0.138278, 0.139708, 0.143988, 0.137819, 0.141013, 0.12999], [0.136104, 0.139635, 0.147291, 0.17541, 0.135345, 0, 0.156033, 0.15923, 0.150207, 0.150578, 0.136218, 0.128162, 0.139499, 0.130331, 0.138461, 0.133372], [0.13785, 0.144094, 0.141504, 0.140778, 0.139473, 0.156033, 0, 0.172838, 0.177661, 0.14624, 0.124683, 0.141052, 0.143781, 0.133345, 0.128425, 0.135457], [0.1359, 0.13827, 0.136099, 0.139217, 0.137404, 0.15923, 0.172838, 0, 0.162814, 0.154834, 0.13149, 0.133739, 0.141394, 0.127495, 0.134251, 0.137112], [0.129561, 0.134079, 0.12451, 0.13595, 0.137059, 0.150207, 0.177661, 0.162814, 0, 0.145129, 0.129512, 0.143372, 0.147626, 0.139202, 0.136019, 0.137473], [0.130072, 0.135737, 0.13495, 0.141595, 0.132094, 0.150578, 0.14624, 0.154834, 0.145129, 0, 0.138168, 0.141627, 0.138613, 0.139953, 0.141049, 0.135209], [0.122706, 0.122706, 0.122706, 0.129701, 0.138278, 0.136218, 0.124683, 0.13149, 0.129512, 0.138168, 0, 0.151435, 0.149054, 0.148704, 0.150927, 0.140313], [0.127095, 0.13448, 0.12794, 0.122706, 0.139708, 0.128162, 0.141052, 0.133739, 0.143372, 0.141627, 0.151435, 0, 0.150428, 0.140229, 0.146598, 0.135881], [0.126207, 0.131666, 0.122706, 0.131605, 0.143988, 0.139499, 0.143781, 0.141394, 0.147626, 0.138613, 0.149054, 0.150428, 0, 0.143604, 0.149609, 0.134722], [0.122927, 0.125851, 0.122706, 0.122809, 0.137819, 0.130331, 0.133345, 0.127495, 0.139202, 0.139953, 0.148704, 0.140229, 0.143604, 0, 0.172858, 0.169226], [0.122809, 0.124441, 0.122706, 0.13014, 0.141013, 0.138461, 0.128425, 0.134251, 0.136019, 0.141049, 0.150927, 0.146598, 0.149609, 0.172858, 0, 0.14728], [0.123364, 0.126234, 0.12527, 0.132785, 0.12999, 0.133372, 0.135457, 0.137112, 0.137473, 0.135209, 0.140313, 0.135881, 0.134722, 0.169226, 0.14728, 0]]
# print(s)
# 1/0

netP = []
netK = []
ISO = []
FNode, K = selectFN(s, c, 0.5 * epsilon1, theta, n, A, le, epsilon2)  # FNode为首节点列表 K为首节点个数

f = open('nltcs1.6.log', 'w')
f.write("Firstnode:%s" % str(FNode))
f.write('\n')
f.close()
FaNode = []
for i in FNode:
    FaNode.append(i)

print(FaNode)
for i in range(K, le):  # 构造完整贝叶斯网络
    print(i)
    Kid, Parent, Iso = GetNet(b, c, A, FaNode, 0.21 * epsilon1, theta, n, K, le, epsilon2)
    if Iso != []:
        ISO = Iso
        f = open('nltcs1.6.log', 'a+')
        f.write('Iso:%s' % (str(ISO)))
        f.close()
        break
    netP.append(Parent)
    netK.append(Kid)
    FaNode.append(Kid)
    print('---------------')
    print(FaNode)
    f = open('nltcs1.6.log', 'a+')
    f.write('%s -------------> %s' % (str(Parent), str(Kid)))
    f.write('\n')
    f.close()
print('*******************************************************************************************111111')
print(netP)
print(netK)
print('*******************************************************************************************111111')
# 得到噪化的概率分布
"""
释放不必要内存 
"""
print('已经构成网络')



"""
以上为构造贝叶斯网络
以下为计算概率分布
"""
print('开始计算首节点概率')
FPro, Alist = GetFNProDist(b, FNode, n, c, epsilon2 / (le - 1 + 1), 2 / n)  # 敏感度待分配


# ---------------------------------------- 代码在此处运行不下去 ------------------------------------------
"""
                              在ProDist.py 的 GetFNProDist 函数中设置断点
"""

print('已经完成首节点概率计算')
#  需要生成概率分布并加入噪声
FkP = []  # 存储分布
FKL = []  # 存储FkP对应属性
CPR = []
JK33 = []
KII = []
for jf in range(len(netK)):  # 得到了分布列表FkP和对应值列表FKL
    print(jf)
    FKPro, FKlist, Jk3, Kii = GetKProDist(netP[jf], netK[jf], n, c, b, epsilon2 / (le - 1 + 1), 2 / n)   # 敏感度待分配
    Cpro = GetCProDist(FKPro, FKlist, Jk3, Kii)
    KII.append(list(Kii))
    FkP.append(FKPro)
    FKL.append(FKlist)
    CPR.append(Cpro)
    JK33.append(Jk3)
Isopro = 0
Isopros = 0
if ISO != 0:
    Isopro, Isopros = GetIsoProDist(ISO, c, b, n, epsilon2 / (le - 1 + 1), 2 / n)

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
    for af1 in FNode:
        synS[af1] = outF[iss]
        iss += 1
    """
    上面循环实现了将首节点放入synS
    下面需要将子节点放入synS
    """
    kss = 0
    for ak in netK:
        fss = netP[kss]  # fss 为父节点
        fflist = []
        for nod1 in fss:  # 取得父节点的值
            fflist.append(synS[nod1])   # fflist是当前元组父节点值
        # CPR[kss]为当前子节点的
        for nums in range(len(JK33[kss])):
            if fflist == JK33[kss][nums]:  # JK33[kss][nums]是父节点值，CPR[kss][nums]为对应条件概率
                synS[ak] = exponentSelectV(CPR[kss][nums], KII[kss])
        kss += 1

    for bk in range(len(Isopros)):
        outS = exponentSelectV(Isopro[bk], Isopros[bk])
        synS[ISO[bk]] = outS


    synlist.append(synS)
for iqq in synlist:
    print(iqq)
f = open('nltcs_1.6_syn.data', 'w')
f.write(str(synlist))
f.close()


etime = time.time()
print('Running time: %s Seconds' % (etime-stime))


