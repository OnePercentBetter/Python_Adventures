import itertools
def Fibonnaci(n):
    if n <= 1:
       return n
    else:
        return (Fibonnaci(n-1)+Fibonnaci(n-2))
total = 0
counter = 1
for i in itertools.count(start=1):
        if Fibonnaci(i) % 2 == 0:
            total += Fibonnaci(i)
            print(total)
            counter += 1
        if total > 4000000:
                break
print(total)
