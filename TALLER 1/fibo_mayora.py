n = int(input("Ingrese un número:"))
print("el siguiente número de la serie de fibonacci más cercano a " + str(n)+" es:")
a = 0
b = 1
i = ("comiemzo")
while i == ("comiemzo"):
    suma = a + b
    if n-suma<=0:
        print(suma)
        i = ("final")
    else:
        a = b
        b = suma
        