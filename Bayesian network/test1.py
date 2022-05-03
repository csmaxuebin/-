import csv
f = open('br2000_1_syn.log', 'r')
b = f.read()
n = eval(b)
f.close()
print(n)
b = [i for i in range(len(n[0]))]
with open("统计.csv",'w',newline='') as t:#numline是来控制空的行数的
    writer=csv.writer(t)#这一步是创建一个csv的写入器
    writer.writerow(b)#写入标签
    writer.writerows(n)#写入样本数据