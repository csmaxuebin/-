import math

b = ['39', 'State-gov', '77516', 'Bachelors', '13', 'Never-married', 'Adm-clerical', 'Not-in-family', 'White', 'Male', '2174', '0', '40', 'United-States', '<=50K'], ['50', 'Self-emp-not-inc', '83311', 'Bachelors', '13', 'Married-civ-spouse', 'Exec-managerial', 'Husband', 'White', 'Male', '0', '0', '13', 'United-States', '<=50K']
c = b
for i in range(len(b)):
    for j in range(len(b[0])):
        # c[i][j] = int(b[i][j])
        if j == 0:
            c[i][j] = math.ceil(int(c[i][j]) / 10)
        if j == 1:
            if c[i][j] == 'Federal-gov' or c[i][j] == 'Local-gov' or c[i][j] == 'State-gov':
                c[i][j] = 'gov'
            elif c[i][j] == 'Self-emp-inc' or c[i][j] == 'Self-emp-not-inc':
                c[i][j] = 'Self-emp'
        if j == 2:
            c[i][j] = math.ceil(int(c[i][j]) / 300000)
        if j == 3:
            if c[i][j] == 'Preschool' or c[i][j] == '1st-4th' or c[i][j] == '5th-6th' or c[i][j] == '7th-8th':
                c[i][j] = 'Junior'
            elif c[i][j] == '9th' or c[i][j] == '10th' or c[i][j] == '11th' or c[i][j] == '12th' or c[i][j] == 'HS-grad':
                c[i][j] = 'HS'
            elif c[i][j] == 'Some-college' or c[i][j] == 'Assoc-voc' or c[i][j] == 'Assoc-acdm':
                c[i][j] = 'college'
            elif c[i][j] == 'Bachelors' or c[i][j] == 'Masters' or c[i][j] == 'Prof-school' or c[i][j] == 'Doctorate':
                c[i][j] = 'Bachelors'
        if j == 4:
            c[i][j] = math.ceil(int(c[i][j]) / 4)
        if j == 5:
            if c[i][j] == 'Married-AF-spouse' or c[i][j] == 'Married-civ-spouse' or c[i][j] == 'Married-spouse-absent':
                c[i][j] = 'Married'
            if c[i][j] == 'Separated' or c[i][j] == 'Widowed' or c[i][j] == 'Divorced':
                c[i][j] = 'Separated'
        if j == 6:
            if c[i][j] == 'Tech-support' or c[i][j] == 'Craft-repair' or c[i][j] == 'Prof-specialty':
                c[i][j] = 'Tech'
            if c[i][j] == 'Handlers-cleaners' or c[i][j] == 'Machine-op-inspct' or c[i][j] == 'Farming-fishing' or c[i][j] == 'Transport-moving'or c[i][j] == 'Priv-house-serv'or c[i][j] == 'Protective-serv':
                c[i][j] = 'Labor'
            if c[i][j] == 'Sales' or c[i][j] == 'Exec-managerial' or c[i][j] == 'Adm-clerical':
                c[i][j] = 'Civil'
        if j == 7:
            if c[i][j] == 'Husband' or c[i][j] == 'Wife' or c[i][j] == 'Own-child':
                c[i][j] = 'Family'
        if j == 8:
            if c[i][j] == 'Amer-Indian-Eskimo' or c[i][j] == 'Asian-Pac-Islander':
                c[i][j] = 'Other'
        if j == 10:
            c[i][j] = math.ceil(int(c[i][j]) / 20000)
        if j == 11:
            c[i][j] = math.ceil(int(c[i][j]) / 1000)
        if j == 12:
            c[i][j] = math.ceil(int(c[i][j]) / 20)
        if j == 13:
            if c[i][j] == 'Outlying-US(Guam-USVI-etc)' or c[i][j] == 'Puerto-Rico':
                c[i][j] = 'Outlying-US'
            elif c[i][j] == 'Cambodia' or c[i][j] == 'China' or c[i][j] == 'Hong' or c[i][j] == 'Japan' or c[i][j] == 'Laos' or c[i][j] == 'Philippines' or c[i][j] == 'South' or c[i][j] == 'Taiwan' or c[i][j] == 'Thailand' or c[i][j] == 'Vietnam':
                c[i][j] = 'ASIA'
            elif c[i][j] == 'Columbia' or c[i][j] == 'Ecuador' or c[i][j] == 'Peru':
                c[i][j] = 'SM'
            elif c[i][j] == 'Cuba' or c[i][j] == 'Dominican-Republic' or c[i][j] == 'El-Salvador' or c[i][j] == 'Guatemala' or c[i][j] == 'Haiti' or c[i][j] == 'Honduras' or c[i][j] == 'Jamaica' or c[i][j] == 'Nicaragua' or c[i][j] == 'Trinadad&Tobago':
                c[i][j] = 'NM'
            elif c[i][j] == 'England' or c[i][j] == 'France' or c[i][j] == 'Germany' or c[i][j] == 'Greece' or c[i][j] == 'Holand-Netherlands' or c[i][j] == 'Hungary' or c[i][j] == 'Ireland' or c[i][j] == 'Italy' or c[i][j] == 'Poland' or c[i][j] == 'Portugal' or c[i][j] == 'Scotland' or c[i][j] == 'Yugoslavia':
                c[i][j] = 'EU'
        #     c[i][j] = math.ceil(c[i][j] / 10)
        # if j == 12:
        #     if c[i][j] == 0:
        #         c[i][j] = 1
        #     c[i][j] = math.ceil(c[i][j] / 10)
        # if j == 2:
        #     if c[i][j] == 0:
        #         c[i][j] = 1
        #     c[i][j] = math.ceil(c[i][j] / 5)

# United-States
# {
# {Outlying-US(Guam-USVI-etc) Puerto-Rico}
# Canada Mexico
# {Cambodia China Hong Japan Laos Philippines South Taiwan Thailand Vietnam}
# {Columbia Ecuador Peru}
# {Cuba Dominican-Republic El-Salvador Guatemala Haiti Honduras Jamaica Nicaragua Trinadad&Tobago}
# {England France Germany Greece Holand-Netherlands Hungary Ireland Italy Poland Portugal Scotland Yugoslavia}
# India Iran}
print(c)