#CANTIDAD DE NUMEROS QUE QUIERE INGRESAR

n = int(input("¿Cuántos números dese ingresar:")) #PEDIMOS AL USUAR
i = 0
suma = 0
pares = 0

for i in range(1, n + 1):
    elementos = int(input("Ingrese números:"))
    if elementos % 2 == 0:
        suma = suma + elementos
        pares = pares + 1
print(suma/pares)