import numpy as np
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
import time


def load_data(filename):
    data1 = np.genfromtxt(filename, delimiter=',')
    # print(data1)
    data = data1[:, [0, 7]]
    x = data[:, 1:]  # 数据特征
    y = data[:, 0].astype(int)  # 标签
    scaler = StandardScaler()
    x_std = scaler.fit_transform(x)  # 标准化
    # 将数据划分为训练集和测试集，test_size=.3表示30%的测试集
    x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=.2)
    return x_train, x_test, y_train, y_test


def svm_c(x_train, x_test, y_train, y_test):
    # rbf核函数，设置数据权重
    svc = SVC(kernel='linear')
    c_range = np.logspace(-5, 15, 3, base=2)
    # gamma_range = np.logspace(-9, 3, 13, base=2)
    # 网格搜索交叉验证的参数范围，cv=3,3折交叉
    param_grid = [{'kernel': ['linear'], 'C': c_range}]
    #param_grid = [{'kernel': ['rbf'], 'C': c_range, 'gamma': gamma_range}]
    grid = GridSearchCV(svc, param_grid, cv=2, n_jobs=-1)
    # 训练模型
    clf = grid.fit(x_train, y_train)
    # 计算测试集精度
    score = grid.score(x_test, y_test)
    print('精度为%s' % score)


if __name__ == '__main__':
    stime = time.time()
    localtime = time.asctime(time.localtime(time.time()))
    print(localtime)
    svm_c(*load_data('br2000_380.csv'))
    etime = time.time()
    print('Running time: %s Seconds' % (etime - stime))
