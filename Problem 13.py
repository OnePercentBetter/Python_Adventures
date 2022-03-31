lis = []
summ  = 0
with open(r'file_path') as f:
    for line in f:
        lis.append(line)
for i in range(0,len(lis)):
    summ += int(lis[i])
print((str(summ)[:10]))
