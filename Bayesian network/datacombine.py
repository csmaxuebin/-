# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 9:56
# @Author  : qixuejian
# @FileName: datacombine.py
# @Software: PyCharm
import math
import csv
f = open('acs_0.4_syn.data', 'r')
a = f.read()
f.close()
b = eval(a)


f1 = open('acs.data', 'r')
a1 = f1.read()
f1.close()
b1 = eval(a)


c = []
for i in range(math.ceil(len(b) * 0.8)):
    c.append(b[i])

for j in range(math.floor(len(b1) * 0.8), len(b1)):
    c.append(b1[j])


s = [is1 for is1 in range(len(c[0]))]
with open("acs0.4_combine.csv",'w',newline='') as t:#numline是来控制空的行数的
    writer = csv.writer(t)#这一步是创建一个csv的写入器
    writer.writerow(s)#写入标签
    writer.writerows(c)#写入样本数据