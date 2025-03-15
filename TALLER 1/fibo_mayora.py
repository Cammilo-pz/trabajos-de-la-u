n = int(input("Ingrese un número:"))# se ingresa un número
print("el siguiente número de la serie de fibonacci más cercano a " + str(n)+" es:")
a = 0
b = 1
i = ("comiemzo")#se crea una variable para iniciar el bucle
while i == ("comiemzo"):
    suma = a + b
    if n-suma<=0: # el numero de la serie mayor a n, será el que al restarselo a n va a dar un numero negativo 
        print(suma)# se imprime
        i = ("final")# se finaliza el bucle
    else:
        a = b
        b = suma
        