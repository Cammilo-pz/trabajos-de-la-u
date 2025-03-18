n= int(input("Ingresa un número:"))
numeros= len(cadena)
m=""
for i in range(numeros-1,-1,-1):
    m= m+cadena[i]
if int(m)==n:
    print("el numero ingresado es capicúa")
    print("su palindromo es: ",m)
else:
    print("El número ingresado no es capicúa")
    




n= int(input("Ingresa un número:"))
cadena= str(n)
m=""
for i in cadena:
    m= i+m
print(m)