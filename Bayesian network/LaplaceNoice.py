# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 16:03
# @Author  : qixuejian
# @FileName: LaplaceNoice.py
# @Software: PyCharm
import numpy as np


def add_lapnoice(epsilon, sensitivity):
    a = np.random.laplace(0, sensitivity / epsilon)
    return a
