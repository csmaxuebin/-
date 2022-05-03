ma = [[0]*len(set(c)) for s1 in range(len(set(d)))]
for elem1 in set(c):
    h += 1
    h1 = 0
    for elem2 in set(d):
        s = 0
        count1 = 0
        while s < len(b):
            if b[s][0] == elem1 and b[s][1] == elem2:
                count1 += 1
            s += 1
        ma[h1][h] = count1
        h1 += 1
print(ma)
mi = 0
w1 = 0
ss2 = 0
t1 = [0]*len(set(d))
while w1 < len(set(d)):
    w2 = 0
    while w2 < len(set(c)):
        t1[w1] += ma[w1][w2]
        w2 += 1
    w1 += 1
print(t1)
t2 = [0]*len(set(c))
while ss2 < len(set(c)):
    ss1 = 0
    while ss1 < len(set(d)):
        t2[ss2] += ma[ss1][ss2]
        ss1 += 1
    ss2 += 1
print(t2)
ww1 = 0
ww2 = 0
mi1 = 0
while ww1 < len(set(d)):
    while ww2 < len(set(c)):
        mi1 += (ma[ww1][ww2]/38000) * math.log((ma[ww1][ww2]/38000)/(t1[ww1]*t2[ww2]/(38000*38000)), 2)

        ww2 += 1
    ww1 += 1
print(mi1)