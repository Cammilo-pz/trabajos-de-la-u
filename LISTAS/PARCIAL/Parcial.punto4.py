#importo el random
from random import randint
#se solicita el valor de n
n = int(input("Ingrese la cantidad de números que desea generar en la lista A: "))
#creo la lista A y la lleno con n numeros aleatorios
A = []
for i in range(n):
    A.append(randint(1, 99))
print("La lista A es: ", A)
#creo la lista B y los lleno con las posiciones de A que sean multiplos de 3
B = []
for i in range(0, n+1):
    if i != 0:
        if (i)%3 == 0:
            if i-1 != 0:
                B.append(A[i-1])
print("La lista B es: ", B)
#EJERCICIO COMPLETO