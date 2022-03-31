import itertools

def isPrime(n):
    for i in range(2, n):
        if n % i == 0: 
            return False
    return n>1
x = 600851475143
for n in itertools.count(0):
    if  isPrime(n):
        if(x % n == 0):
            print(x / n, n)
        else:
            continue
