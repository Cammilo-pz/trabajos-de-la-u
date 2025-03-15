n = int(input("Ingrese un número:"))
print("los números de la serie de fibonacci menores que "+ str(n)+ " son:")
a = 0
b = 1
print(a)
print(b)
i = a
while i < n:
    suma = a + b
    a = b
    b = suma
    if b < n:
        print(b)
    else:
        i = n
