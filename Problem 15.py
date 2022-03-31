"""Project Euler problem 15"""
def sum(n):
    welp = n**1000
    total = 0
    for i in str(welp):
        total += int(i)
    return total
print(sum(2))
