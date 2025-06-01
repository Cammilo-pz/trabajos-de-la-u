#importo las funciones y el random
from random import randint
import numpy as np

#Defino la funcion para ordenar la matriz y poderla ver como matriz nxn
def print_2dlist(L):
    filas = len(L)
    if filas > 0 :
        cols = len(L[0])
        print("[", end = "")
        for i in range(filas):
            print("[ ", end = "")
            for j in range(cols):
                print(f" {L[i][j]} ", end = "")
            if i < (filas - 1) :
                print("]")
            else :
                print("]", end="")
        print("]")
    else :
        print("La matriz no se puede imprimir porque no tiene filas")
#solicito el valor de n 
filas1 = int(input("ingrese una cantidad de filas y columnas nxn: "))
cols1 = int(filas1)
#filas será igual al valor de columnas
lista2d = [ [ 0 ]*cols1 for n in range(filas1) ]
#Relleno la matriz con ceros y luego genero un valor elatoria para cada una de las posiciones de la matriz
A = [ [ 0 ]*cols1 for n in range(filas1) ]
for i in range(filas1):
    for j in range(cols1):
        A[i][j] = randint(1, 99)
print(A)
# aplico la funcion a la lista para verla como una matriz
print_2dlist(A)

D_principal = 0
D_secundaria = 0
#obtengo el promedio de la primera diagonal
for i in range(filas1):
    D_principal += A[i][i]
promedioD_principal = D_principal/filas1
print("El promedio de la diagonal principal es: ", promedioD_principal)

#obtengo el promedio de la segunda diagonal
for j in range(filas1-1, -1, -1):
    for i in range(filas1):
        if i+j == filas1-1:
            D_secundaria += A[j][i]
promedioD_secundaria = D_secundaria/filas1
print("El promedio de la diagonal secundaria es: ", promedioD_secundaria)
#imprimí los promedios de las dos diagonales por aparte

#EJERCICIO COMPLETO