# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 12:53
# @Author  : qixuejian
# @FileName: data_handing.py
# @Software: PyCharm
# ['39', 'State-gov', '77516', 'Bachelors', '13', 'Never-married', 'Adm-clerical', 'Not-in-family', 'White', 'Male', '2174', '0', '40', 'United-States', '<=50K']

import math
f = open('br2000.data', 'r')
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
        if j == 2:
            if c[i][j] == 0:
                c[i][j] = 1
            c[i][j] = math.ceil(c[i][j] / 5)
f = open('br2000_handled.data', 'w')
f.write(str(c))
f.close()