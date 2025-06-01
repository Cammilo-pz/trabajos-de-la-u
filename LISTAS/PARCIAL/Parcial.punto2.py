
#importo el random
from random import randint
#se solicita el valor de n
n = int(input("Ingrese la cantidad de números que desea generar en la lista A: "))
#creo la lista A y la lleno con n numeros aleatorios
A = []
for i in range(n):
    A.append(randint(1, 100))
print(A)
B = []
C = []
#Distribuyo la lista 
for i in range(n):
    if i%2 == 0:
        B.append(A[i])
    else:
        C.append(A[i])
print("tenga en cuenta que la lista inicia en la posiciónn 0, por lo cúal el primer valor es par")
#teniendo en cuenta la posición 0
print("")
sum = 0
print("la lista con numeros en posiciones pares es",B)
for i in B:
    sum += i
promedio = sum/len(B)
print("El promedio de los pares es: ", promedio) 
print("")
sum = 0
print("la lista con numeros en posiciones impares es",C)
for i in C:
    sum += i
print("La suma de los impares es: ",sum)
print(" ")

D= []
for i in B:
    D.append(i/(max(A)))
print(D)
print("")
M= []
for i in C:
    M.append(i/(min(A)))
print(M)
print("")
Lista_final = []
if len(B)> len(C):
    for i in range(len(B)):
        Lista_final.append(D[i])
        Lista_final.append(M[i])
else:
    for i in range(len(C)):
        Lista_final.append(D[i])
        Lista_final.append(M[i])
print(Lista_final)
""". Construir un programa que lea una lista de elementos enteros de
longitud n (n debe ser pedida al usuario) y calcule el promedio de los
elementos en posiciones pares y la suma de los elementos en las
posiciones impares de la lista. También debe crear una segunda lista
en la que se guarden los valores resultantes de dividir los elementos en
las posiciones pares por el máximo de los elementos y los impares por
el mínimo. Mostrar todos los resultados en pantalla."""