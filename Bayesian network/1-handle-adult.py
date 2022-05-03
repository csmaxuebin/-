# python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 14:59
# @Author  : qixuejian
# @FileName: 1-handle-adult.py
# @Software: PyCharm
import math
f = open('adult.data', 'r')
a = f.read()
f.close()
b = eval(a)
c = b
for i in range(len(b)):
    for j in range(len(b[0])):
        # c[i][j] = int(b[i][j])
        if j == 0:
            c[i][j] = math.ceil(int(c[i][j]) / 10)
        if j == 1:
            if c[i][j] == 'Federal-gov' or c[i][j] == 'Local-gov' or c[i][j] == 'State-gov':
                c[i][j] = 0
            elif c[i][j] == 'Self-emp-inc' or c[i][j] == 'Self-emp-not-inc':
                c[i][j] = 2
            elif c[i][j] == 'Private':
                c[i][j] = 1
            elif c[i][j] == 'Without-pay':
                c[i][j] = 3
        if j == 2:
            c[i][j] = math.ceil(int(c[i][j]) / 200000)
        if j == 3:
            if c[i][j] == 'Preschool':
                c[i][j] = 0
            elif c[i][j] == '1st-4th':
                c[i][j] = 1
            elif c[i][j] == '5th-6th' or c[i][j] == '7th-8th':
                c[i][j] = 2
            elif c[i][j] == '9th' or c[i][j] == '10th' or c[i][j] == '11th' or c[i][j] == '12th':
                c[i][j] = 3
            elif c[i][j] == 'HS-grad':
                c[i][j] = 4
            elif c[i][j] == 'Some-college' or c[i][j] == 'Assoc-voc' or c[i][j] == 'Assoc-acdm':
                c[i][j] = 5
            elif c[i][j] == 'Bachelors':
                c[i][j] = 6
            elif c[i][j] == 'Masters' or c[i][j] == 'Prof-school' or c[i][j] == 'Doctorate':
                c[i][j] = 7
        if j == 4:
            c[i][j] = math.ceil(int(c[i][j]) / 2)
        if j == 5:
            if c[i][j] == 'Never-married':
                c[i][j] = 0
            elif c[i][j] == 'Married-AF-spouse' or c[i][j] == 'Married-civ-spouse' or c[i][j] == 'Married-spouse-absent':
                c[i][j] = 1
            elif c[i][j] == 'Separated' or c[i][j] == 'Widowed' or c[i][j] == 'Divorced':
                c[i][j] = 2
        if j == 6:
            if c[i][j] == 'Adm-clerical':
                c[i][j] = 0
            elif c[i][j] == 'Armed-Forces':
                c[i][j] = 1
            elif c[i][j] == 'Craft-repair':
                c[i][j] = 2
            elif c[i][j] == 'Exec-managerial':
                c[i][j] = 3
            elif c[i][j] == 'Farming-fishing':
                c[i][j] = 4
            elif c[i][j] == 'Handlers-cleaners':
                c[i][j] = 5
            elif c[i][j] == 'Machine-op-inspct':
                c[i][j] = 6
            elif c[i][j] == 'Other-service':
                c[i][j] = 7
            elif c[i][j] == 'Priv-house-serv':
                c[i][j] = 8
            elif c[i][j] == 'Prof-specialty':
                c[i][j] = 9
            elif c[i][j] == 'Protective-serv':
                c[i][j] = 10
            elif c[i][j] == 'Sales':
                c[i][j] = 11
            elif c[i][j] == 'Tech-support':
                c[i][j] = 12
            elif c[i][j] == 'Transport-moving':
                c[i][j] = 13
            # if c[i][j] == 'Tech-support' or c[i][j] == 'Craft-repair' or c[i][j] == 'Prof-specialty':
            #     c[i][j] = 0
            # elif c[i][j] == 'Handlers-cleaners' or c[i][j] == 'Machine-op-inspct' or c[i][j] == 'Farming-fishing' or c[i][j] == 'Transport-moving'or c[i][j] == 'Priv-house-serv'or c[i][j] == 'Protective-serv':
            #     c[i][j] = 1
            # elif c[i][j] == 'Sales' or c[i][j] == 'Exec-managerial' or c[i][j] == 'Adm-clerical':
            #     c[i][j] = 2
            # elif c[i][j] == 'Other-service':
            #     c[i][j] = 3
            # elif c[i][j] == 'Armed-Forces':
            #     c[i][j] = 4
        if j == 7:
            if c[i][j] == 'Husband':
                c[i][j] = 0
            elif c[i][j] == 'Wife':
                c[i][j] = 1
            elif c[i][j] == 'Own-child':
                c[i][j] = 2
            elif c[i][j] == 'Other-relative':
                c[i][j] = 3
            elif c[i][j] == 'Not-in-family':
                c[i][j] = 4
            elif c[i][j] == 'Unmarried':
                c[i][j] = 5
        if j == 8:
            if c[i][j] == 'Amer-Indian-Eskimo' or c[i][j] == 'Asian-Pac-Islander' or c[i][j] == 'Other':
                c[i][j] = 2
            elif c[i][j] == 'White':
                c[i][j] = 0
            elif c[i][j] == 'Black':
                c[i][j] = 1
        if j == 9:
            if c[i][j] == 'Female':
                c[i][j] = 0
            elif c[i][j] == 'Male':
                c[i][j] = 1
        if j == 10:
            c[i][j] = math.ceil(int(c[i][j]) / 10000)
        if j == 11:
            c[i][j] = math.ceil(int(c[i][j]) / 1000)
        if j == 12:
            c[i][j] = math.ceil(int(c[i][j]) / 10)
        if j == 13:
            if c[i][j] == 'Outlying-US(Guam-USVI-etc)' or c[i][j] == 'Puerto-Rico':
                c[i][j] = 1
            elif c[i][j] == 'Cambodia' or c[i][j] == 'China' or c[i][j] == 'Hong' or c[i][j] == 'Japan' or c[i][j] == 'Laos' or c[i][j] == 'Philippines' or c[i][j] == 'South' or c[i][j] == 'Taiwan' or c[i][j] == 'Thailand' or c[i][j] == 'Vietnam':
                c[i][j] = 4
            elif c[i][j] == 'Columbia' or c[i][j] == 'Ecuador' or c[i][j] == 'Peru':
                c[i][j] = 5
            elif c[i][j] == 'Cuba' or c[i][j] == 'Dominican-Republic' or c[i][j] == 'El-Salvador' or c[i][j] == 'Guatemala' or c[i][j] == 'Haiti' or c[i][j] == 'Honduras' or c[i][j] == 'Jamaica' or c[i][j] == 'Nicaragua' or c[i][j] == 'Trinadad&Tobago':
                c[i][j] = 6
            elif c[i][j] == 'England' or c[i][j] == 'France' or c[i][j] == 'Germany' or c[i][j] == 'Greece' or c[i][j] == 'Holand-Netherlands' or c[i][j] == 'Hungary' or c[i][j] == 'Ireland' or c[i][j] == 'Italy' or c[i][j] == 'Poland' or c[i][j] == 'Portugal' or c[i][j] == 'Scotland' or c[i][j] == 'Yugoslavia':
                c[i][j] = 7
            elif c[i][j] == 'United-States':
                c[i][j] = 0
            elif c[i][j] == 'Canada':
                c[i][j] = 2
            elif c[i][j] == 'Mexico':
                c[i][j] = 3
            elif c[i][j] == 'India':
                c[i][j] = 8
            elif c[i][j] == 'Iran':
                c[i][j] = 9
        if j == 14:
            if c[i][j] == '<=50K':
                c[i][j] = 0
            elif c[i][j] == '>50K':
                c[i][j] = 1
f = open('adult_handled1.data', 'w')
f.write(str(c))
f.close()
# United-States
# {Outlying-US(Guam-USVI-etc) Puerto-Rico}
# Canada
# Mexico
# {Cambodia China Hong Japan Laos Philippines South Taiwan Thailand Vietnam}
# {Columbia Ecuador Peru}
# {Cuba Dominican-Republic El-Salvador Guatemala Haiti Honduras Jamaica Nicaragua Trinadad&Tobago}
# {England France Germany Greece Holand-Netherlands Hungary Ireland Italy Poland Portugal Scotland Yugoslavia}
# India
# Iran