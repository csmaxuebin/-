# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 15:57
# @Author  : qixuejian
# @FileName: 1-salarysvm.py
# @Software: PyCharm
import numpy as np
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
import time


def load_data(filename):
    data1 = np.genfromtxt(filename, delimiter=',')


    data = data1[:, [14, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]]



    x = data[:, 1:]  # 数据特征
    y = data[:, 0].astype(int)  # 标签
    scaler = StandardScaler()
    x_std = scaler.fit_transform(x)  # 标准化
    x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=.2)
    return x_train, x_test, y_train, y_test


def svm_c(x_train, x_test, y_train, y_test):
    # svc = SVC(kernel='linear', decision_function_shape='ovr')
    svc = SVC(kernel='linear', C=5, decision_function_shape='ovr')
    clf = svc.fit(x_train, y_train)
    score = svc.score(x_test, y_test)
    print('精度为%s' % score)


if __name__ == '__main__':
    stime = time.time()
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    svm_c(*load_data('adultZ1.6_combine.csv'))
    etime = time.time()
    print('Running time: %s Seconds' % (etime - stime))
