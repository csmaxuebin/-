# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 17:42
# @Author  : qixuejian
# @FileName: handleadult.py
# @Software: PyCharm
import math
f = open('adult.data', 'r')
a = f.read()
f.close()
b = eval(a)
c = b
for i in range(len(b)):
    for j in range(len(b[0])):
        c[i][j] = int(b[i][j])
        if j == 4:
            if c[i][j] == 0:
                c[i][j] = 1
            c[i][j] = math.ceil(c[i][j] / 10)
        if j == 10:
            if c[i][j] == 0:
                c[i][j] = 1
            c[i][j] = math.ceil(c[i][j] / 10)
        if j == 12:
            if c[i][j] == 0:
                c[i][j] = 1
            c[i][j] = math.ceil(c[i][j] / 10)
        if j == 3:
            if c[i][j] == 0:
                c[i][j] = 1
            c[i][j] = math.ceil(c[i][j] / 3)
f = open('br2000_1_handled1.data', 'w')
f.write(str(c))
f.close()
