a = []
r = []
for n in range(100,999):
    for i in range(100,999):
        y = n * i
        if str(y) == str(y)[::-1]:
            a.insert(0,y)
            r.insert(0,(y,n,i))
a.sort()
print(a)
print(max(a))
r.sort()
print(max(r))
