# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/22 10:39
# @Author  : qixuejian
# @FileName: listTocsv.py
# @Software: PyCharm
# f = open('br2000_1_syn.log', 'r')
# a = f.read()
# f.close()
# s = open('br2000_1_syn.csv', 'r')
# for i in a:
import csv
import codecs
import pandas as pd
import numpy as np

f = open('acs.data', 'r')
b = f.read()
c = eval(b)
f.close()

b = [i for i in range(len(c[0]))]
with open("acs.csv",'w',newline='') as t:#numline是来控制空的行数的
    writer = csv.writer(t)#这一步是创建一个csv的写入器
    writer.writerow(b)#写入标签
    writer.writerows(c)#写入样本数据























# def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
#     file = open(filename,'a')
#     for i in range(len(data)):
#         s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
#         s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
#         file.write(s)
#     file.close()
#     print("保存文件成功")
#
#
# def data_write_csv(file_name, datas):  # file_name为写入CSV文件的路径，datas为要写入数据列表
#     file_csv = codecs.open(file_name,'w+','utf-8')  # 追加
#     writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
#     for data in datas:
#         writer.writerow(data)
#     print("保存文件成功，处理结束")
#
#
# f = open('br2000_1_syn.log', 'r')
# a = f.read()
# f.close()
#
# text_save('br2000_1_syn.txt', a)
# f = open('br2000_1_syn.txt', 'r')
# c = f.read()
# f.close()
#
# data_write_csv('br2000_1_syn.csv', c)

# name = ['%s' % i for i in range(len(a[0]))]
# test = pd.DataFrame(columns=name, data= a)
# test.to_csv('br2000_1_syn.csv')