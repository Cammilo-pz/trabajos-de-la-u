import random as rnd
import matplotlib.pyplot as plt

A = []
n= int(input("Ingresa la cantidad de valores a tener en cuenta: "))
for i in range(n):
    A.append((rnd.randint(150,210))/100)
    

B = []
for i in range(n):
    B.append((rnd.randint(50,120)))

print("La altura de las personas es: ")
print(A)
print(" ")
print("El peso de las personnas es: ")
print(B)


sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
puntos=0
for j in range(len(A) and len(B)):
    sum1= sum1 + A[j]*B[j]
    sum2= sum2 + A[j]
    sum3= sum3 + B[j]
    sum4= sum4 + (A[j]**2)
sum5= (sum2**2)
m= ((n*sum1)-(sum2*sum3))/((n*sum4)-sum5)
b1= ((sum3*sum4)-(sum2*sum1))/((n*sum4)-sum5)
b2= ((sum3-(m*sum2))/n)
print(m)
print(b2)
maximoenx=22
X=[]
Y=[]
for i in range (15, maximoenx): #si quiero ver solo la parte del rango utilizado coloco desde el minimo de altura osea 15 o 1.5 
    X.append(i/10)
for j in range (len(X)):
    Y.append(m*(X[j])+b2)
        
print(X)
print(Y)

plt.plot(A, B, "b*", X, Y, "g-")
plt.show()