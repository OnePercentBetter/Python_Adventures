lis = (11,12,13,14,15,16,17,18,19,20)
def smallest():
    count = 0
    n = 2520
    while count<= 2:
        for i in lis:
            if n % i == 0:
                count += 1
                print(count)
                print(n)
            else:
                count = 0
                break
            if count == 20:
                break
                return n
        n +=2520
print(smallest())
