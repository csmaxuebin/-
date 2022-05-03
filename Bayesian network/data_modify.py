f = open('acs.dat', 'r')
a = f.readlines()
print(a)
f.close()
c = []

for i in a:
    b = i.strip('\n')
    b = b.split('\t')
    b = list(b)
    c.append(b)
print(c)
f = open('acs.data', 'w')
f.write(str(c))
f.close()
