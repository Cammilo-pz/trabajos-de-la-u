import random as rnd

n = 10
L = []
for i in range(n):
    L.append(int(30*rnd.random()))
print(L)

n = len(L)
for i in range(n - 1):
    for j in range(n - i - 1):
       
        if L[j] > L[j + 1]:
            L[j], L[j + 1] = L[j + 1], L[j]
            
    

print(L)
