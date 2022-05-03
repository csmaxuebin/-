# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 12:10
# @Author  : qixuejian
# @FileName: test4.py
# @Software: PyCharm
import math
import pandas as pd
import numpy as np
c = [0.19732, 0.153783, 0.147378, 0.132562, 0.07266, 0.064115]

d = [0.242342, 0.178682, 0.151135, 0.138873, 0.11369, 0.091947]
ax2 = plt.subplot(1, 2, 2)
ax2.plot(x, c, label='FPrivBayes', linestyle='--')
ax2.plot(x, d, label='Privbayes')
_xtick_labels = [0.05, 0.1, 0.2, 0.4, 0.8, 1.6]
plt.xticks(x, _xtick_labels)
plt.legend(loc=0) # upperleft : 左上角
plt.ylabel('average variation distance', fontsize=20)
plt.xlabel('privacy budget ε', fontsize=20)
plt.title('BR2000,Q3',  y=-0.1, fontsize=30)
plt.show()