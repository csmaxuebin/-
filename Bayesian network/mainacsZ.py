import time
import numpy as np
import gc
from ScoreCalculator import CalScore
from FNZ import selectFNZ
from BNZ import GetNet, GetFKNet
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
epsilon = 0.4    # 隐私预算37开 网络阶段3 分布7
"""
1.网络阶段隐私预算： 首节点分配30% 其余均分70%  -- 即首节点分配 0.3X0.3=0.09  --其余分布分配 0.21 / d-k
2.分布阶段隐私预算：一共d-k+1个分布均分  -- 即每个分布分配 0.7 / d-k+1
"""
epsilon1 = 0.3 * epsilon
epsilon2 = 0.7 * epsilon

theta = 4

netP = []
netK = []
ISO = []
FaNode = []
FiNode = []

FNode, K = selectFNZ(c, epsilon1, theta, n, A, le, epsilon2)  # FNode为首节点列表 K为首节点个数
FiNode.append(FNode)
for ki in range(1, K + 1):
    F1node1 = GetFKNet(b, c, A, FiNode, epsilon1, theta, n, ki, le, epsilon2, K)
    FiNode.append(F1node1)

f = open('nltcsZ0.4.log', 'w')
f.write("Firstnode:%s" % str(FiNode))
f.write('\n')
f.close()
for fi in FiNode:
    FaNode.append(fi)
for i in range(K + 1, le):  # 构造完整贝叶斯网络
    print(i)
    Kid, Parent, Iso = GetNet(b, c, A, FaNode, 0.21 * epsilon1, theta, n, K, le, epsilon2)
    if Iso != []:
        ISO = Iso
        f = open('nltcsZ0.4.log', 'a+')
        f.write('Iso:%s' % (str(ISO)))
        f.close()
        break
    netP.append(Parent)
    netK.append(Kid)
    FaNode.append(Kid)
    print('---------------')
    print(FaNode)
    f = open('nltcsZ0.4.log', 'a+')
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
FPro, Alist = GetFNProDist(b, FiNode, n, c, epsilon2 / (le - K), 2 / n)  # 敏感度待分配


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
    FKPro, FKlist, Jk3, Kii = GetKProDist(netP[jf], netK[jf], n, c, b, epsilon2 / (le - K), 2 / n)   # 敏感度待分配
    Cpro = GetCProDist(FKPro, FKlist, Jk3, Kii)
    KII.append(list(Kii))
    FkP.append(FKPro)
    FKL.append(FKlist)
    CPR.append(Cpro)
    JK33.append(Jk3)
Isopro = 0
Isopros = 0
if ISO != 0:
    Isopro, Isopros = GetIsoProDist(ISO, c, b, n, epsilon2 / (le - K), 2 / n)

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
    for af1 in FiNode:
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
f = open('nltcsZ0.4_syn.data', 'w')
f.write(str(synlist))
f.close()


etime = time.time()
print('Running time: %s Seconds' % (etime-stime))


