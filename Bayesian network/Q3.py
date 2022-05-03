# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 17:51
# @Author  : qixuejian
# @FileName: Q3.py
# @Software: PyCharm
import time
import numpy as np
from itertools import product as pr
f = open('acs_0.2_syn.data', 'r')
a = f.read()
f.close()
b = eval(a)
c2 = np.array(b)

f1 = open('acs.data', 'r')
a1 = f1.read()
f1.close()
b1 = eval(a1)
c1 = np.array(b1)
n = len(b)
le = len(b[0])
A = [a1 for a1 in range(le)]
result = []
stime = time.time()
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
for i in range(le - 2):
    for j in range(i + 1, le - 1):
        for k in range(j + 1, le):
        # yuan1 = []
        # yuan2 = []
            sety = []
            listy = []
            result1 = 0
        # for num in range(n):
        #     yuan1.append(b1[num][i])
        #     yuan2.append(b1[num][j])
            sety.append(set(c1[:, i]))
            sety.append(set(c1[:, j]))
            sety.append(set(c1[:, k]))
            for i1 in pr(* sety):
                listy.append(list(i1))
            numT1 = [0 for nu1 in range(len(listy))]
            numT2 = [0 for nu1 in range(len(listy))]
            t = 0
            for i2 in listy:
                for num in range(n):
                    if [b1[num][i], b1[num][j], b1[num][k]] == i2:
                        numT1[t] += 1
                    if [b[num][i], b[num][j], b[num][k]] == i2:
                        numT2[t] += 1
                t += 1
            for tot in range(len(numT1)):
                result1 += (np.abs(numT1[tot] - numT2[tot]) / 38000 / 2)
            result.append(result1)
print('0.1:')
print(result)
average_a = np.mean(result)
print(average_a)
etime = time.time()
print('Running time: %s Seconds' % (etime - stime))
