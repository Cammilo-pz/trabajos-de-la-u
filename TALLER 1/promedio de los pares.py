#CANTIDAD DE NUMEROS QUE QUIERE INGRESAR
n = int(input("¿Cuántos números desea ingresar:")) 
i = 0
suma = 0
pares = 0

for i in range(1, n + 1):
    elementos = int(input("Ingrese números:"))# ingresa la cantidad de numeros establecida
    if elementos % 2 == 0: #comprueba si es par
        suma = suma + elementos
        pares = pares + 1
print("el promedio de los numeros pares es: ",(suma/pares))# se saca el promedio de solo los pares