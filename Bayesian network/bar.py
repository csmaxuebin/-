# python3
# -*- coding: utf-8 -*-
# @Time    : 2021/3/24 21:34
# @Author  : qixuejian
# @FileName: bar.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
waters = ('0.1', '0.4', '0.8')
buy_number_male = [3.28, 9.45, 24.23]
buy_number_female = [1.68, 4.82, 12.94]

bar_width = 0.3  # 条形宽度
index_male = np.arange(len(waters))  # 男生条形图的横坐标
index_female = index_male + bar_width  # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_male, height=buy_number_male, width=bar_width,  label='PrivBayes')
plt.bar(index_female, height=buy_number_female, width=bar_width,  label='FAPrivBayes')

plt.legend()  # 显示图例
plt.xticks(index_male + bar_width / 2, waters)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('runtime')  # 纵坐标轴标题

plt.show()
