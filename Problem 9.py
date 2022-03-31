v1,v2,v3 = 0,0,0
#Has to meet two conditions, one is that the sum is 1000 and the sum of A squared 
# and b squared is c squared
for i in range(0,500): #With the assumption that c won't be bigger than 500
    v1 = i*i
    for j in range(i,500):
        v2 = j*j
        for k in range(j,500):
            v3 = k*k
            if v1 + v2 == v3:
                if i + j + k == 1000:
                    print(i,j,k)
            
