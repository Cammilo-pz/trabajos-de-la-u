from random import randint
import numpy as np

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

filas1 = int(input("ingrese una cantidad de filas y columnas nxn: "))
cols1 = int(filas1)

lista2d = [ [ 0 ]*cols1 for n in range(filas1) ]

A = [ [ 0 ]*cols1 for n in range(filas1) ]
for i in range(filas1):
    for j in range(cols1):
        A[i][j] = randint(1, 99)
print(A)

print_2dlist(A)
Diagonal = 0
for i in range(filas1):
    D_principal += A[i][i]
for j in range(cols1):
    
print(Diagonal)       