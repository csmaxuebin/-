# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 10:35
# @Author  : qixuejian
# @FileName: chuangjiancsv.py
# @Software: PyCharm
import csv
from sklearn.datasets import make_blobs
from matplotlib import pyplot


data,target=make_blobs(n_samples=100,n_features=2,centers=3,cluster_std=[1.0,3.0,2.0])

with open('test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for point in data:
        writer.writerow(point)

pyplot.scatter(data[:,0],data[:,1],c=target);
pyplot.show()
