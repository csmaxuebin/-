import math
import time
from sklearn import metrics as mr
f = open('br2000_1.data', 'r')
a = f.read()
f.close()
b = eval(a)
i = 0
j = 0
c = []
d = []
h = -1
# stime = time.time()


def CalMI(list1, first, second):
    i1 = 0
    mi = 0
    b1 = list1
    fir = first
    sec = second
    while i1 < len(b1):
        c.append(b[i1][fir])
        d.append(b[i1][sec])
        i1 += 1
    mi = mr.mutual_info_score(d, c)
    return mi


line1 = 0
tt = 0
MIarr = [[0] * len(b[1]) for sss in range(len(b[1]))]
while line1 < (len(b[1])):
    line2 = 0
    while line2 < (len(b[1])):
        if line1 == line2:
            MIarr[line1][line2] = 0
        elif line2 > line1:
            MIarr[line1][line2] = CalMI(b, line1, line2)
            MIarr[line2][line1] = MIarr[line1][line2]
            print(tt)
            tt += 1
        line2 += 1
    line1 += 1

for ii in range(len(b[1])):
    print(MIarr[ii])

print('**********************************')
MIarr1 = [[0] * len(b[1]) for sss in range(len(b[1]))]
for ii1 in range(len(b[1])):
    for ii2 in range(len(b[1])):
        if MIarr[ii1][ii2] > 0.006:
            MIarr1[ii1][ii2] = 1
        else:
            MIarr1[ii1][ii2] = 0
for ii2 in range(len(b[1])):
    print(MIarr1[ii2])


print('**********************************')
SIM = [0] * len(b[1])
for si in range(len(b[1])):
    for sii in range(len(b[1])):
        SIM[si] += MIarr[si][sii]
print(SIM)
# ma = [[0]*len(set(c)) for s1 in range(len(set(d)))]  # 此段得到两个属性的概率分布矩阵
# for elem1 in set(c):
#     h += 1
#     h1 = 0
#     for elem2 in set(d):
#         s = 0
#         count1 = 0
#         while s < len(b):
#             if b[s][1] == elem1 and b[s][1] == elem2:
#                 count1 += 1
#             s += 1
#         ma[h1][h] = count1
#         h1 += 1
# # print(ma)  # 输出概率分布矩阵
#
# w1 = 0
# ss2 = 0
# t1 = [0]*len(set(d))
# while w1 < len(set(d)):   # d属性概率分布由t1表示
#     w2 = 0
#     while w2 < len(set(c)):
#         t1[w1] += ma[w1][w2]
#         w2 += 1
#     w1 += 1
# # print(t1)
# t2 = [0]*len(set(c))   # c属性概率分布由t2表示
# while ss2 < len(set(c)):
#     ss1 = 0
#     while ss1 < len(set(d)):
#         t2[ss2] += ma[ss1][ss2]
#         ss1 += 1
#     ss2 += 1
# # print(t2)
# ww1 = 0  # ww1 表示d属性分布下标
# mi1 = 0
# mit = 0
# while ww1 < len(set(d)):
#     ww2 = 0   # ww2 表示c属性分布下标
#     while ww2 < len(set(c)):
#         if t1[ww1] == 0 or t2[ww2] == 0 or ma[ww1][ww2] == 0:
#             mit = 0
#         else:
#             mit = (float(ma[ww1][ww2])/38000.0) * math.log((ma[ww1][ww2])/(t1[ww1]*t2[ww2]/38000), 2)
#         mi1 += mit
#         ww2 += 1
#     ww1 += 1
# print(mi1)
# etime = time.time()
# t_time = etime - stime
# print("程序运行时间：%.8s s" % t_time)