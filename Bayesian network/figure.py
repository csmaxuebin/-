# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 17:01
# @Author  : qixuejian
# @FileName: figure.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def to_percent(temp, position):
    return '%1.0f' % (100*temp) + '%'


a1 = [0.712632,	0.752845,	0.770815,	0.775208,	0.787182,	0.79227]
x = range(0, 6)
b1 = [0.695329,	0.732789,	0.750463,	0.758341	,0.767126	,0.784059]
b2 = [0.7093787,0.749787,0.77187,0.775787,0.788787,0.7927787]
b3 = [0.733329,0.7675789,0.778463,0.78969341,0.793126,0.795463]

c1 = [0.800463,0.800463,0.800463,0.800463,0.800463,0.800463]
d = [1, 1, 1, 1, 1, 1]
at = np.array(a1)
bt = np.array(b1)
ct = np.array(c1)
t2 = np.array(b2)
t3 = np.array(b3)
dt = np.array(d)
a = list(dt - at)
b = list(dt - bt)
c = list(dt - ct)
c11 = list(dt - t2)

c21 = list(dt - t3)
plt.plot(x, a, label='APrivbayes', linestyle='--')

plt.plot(x, c11, label='FAPrivbayes')
plt.plot(x, c21, label='JTFAPB')
plt.plot(x, b, label='Privbayes')
plt.plot(x, c, label='NoPrivacy')

_xtick_labels = [0.05, 0.1, 0.2, 0.4, 0.8, 1.6]
plt.xticks(x, _xtick_labels)
plt.legend(loc=0) # upperleft : 左上角
plt.ylabel('misclassification rate')
plt.xlabel('privacy budget ε')
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.savefig('nltcs-traveling')
plt.show()