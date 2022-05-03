# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 17:22
# @Author  : qixuejian
# @FileName: figureq.py
# @Software: PyCharm

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


a1 = [0.109112	,0.077237	,0.060075	,0.05149	,0.03409	,0.030956]
x = range(0, 6)
b1 = [0.130916	,0.096322	,0.085157	,0.058319	,0.052997	,0.043125]
b2 = [0.109052,0.0705102,0.0620932,0.051326,0.0357528,0.03279]
b3 = [0.086861,0.065102,0.055132,0.040326,0.030528,0.0298059]
plt.plot(x, a1, label='APrivbayes', linestyle='--')
plt.plot(x, b1, label='Privbayes')
plt.plot(x, b2, label='FAPrivbayes')
plt.plot(x, b3, label='JTFAPB')
_xtick_labels = [0.05, 0.1, 0.2, 0.4, 0.8, 1.6]
plt.xticks(x, _xtick_labels)
# plt.tick_params(labelsize=14)
plt.legend(loc=0) # upperleft : 左上角
plt.ylabel('average variation distance', fontsize=10)
plt.xlabel('privacy budget ε', fontsize=10)
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
plt.savefig('nltcs-Q3', dpi=300)
plt.show()