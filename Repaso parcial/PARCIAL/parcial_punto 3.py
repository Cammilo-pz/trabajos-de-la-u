print(" ")
n = int(input("Ingrese un número y obtendrás cuales de sus cifras son pares y cuales impares: "))#ingresa un número
print(" ")#para que se vea organizado
m= str(n) #m sera la cadena de n
numero= len(m) #numero sera la posición en que se encuentra cada número de la cadena
for i in m:
    if int(i)%2==0: #si el entero de i es divisible entre 2 es par
        print(f"El número {i} es par")
    else:# si no entonces es impar
        print(f"El número {i} es impar")
print(" ")
print("La cantidad de cifras del numero ingresado es de:",numero)# acá aclaramos la cantidad de cifras de numero ingresado
print(" ")







 