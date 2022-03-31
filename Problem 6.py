def sum(n):
    count = 0
    for i in range(0,n+1):
        count += i*i
    return count
print(sum(10))

def square(n):
    count = 0
    for i in range(0,n+1):
        count += i
    return count**2
print(square(100)-sum(100))
