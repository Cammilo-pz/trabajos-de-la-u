#vamos a imprimir las indicaciones con las que manejaremos el programa
print("Escoge una de las siguiente operaciones digitando el número 1 o el número 2:")
print("Operación 1: Comprobar si el número es par o impar")
print("Operación 2: comprobar si el número es primo o no")
print(" ")
m= int(input("operación seleccionada:"))#Ingresamos el numero de la operación si es la primera 1 si es la segunda 2
print(" ")
if m==1:#realizamos la primera condición si se cumple que m==1
    numero = int(input("Ingresa un número: "))# ingresamos un numero
    print(" ")
    if numero<0: #si el numero es negativo, mencionamos que es invalido
        print("El número ingresado no es válido debe ser positivo")
        m!= 1
        
    else:# si el numero es positivo hacemos la operación que verifica si es par o impar
        if numero%2==0:
            print("El número ",(numero),"es par")
        else:
            print("El número",(numero),"es impar")
            
elif m==2:#realizamos la segunda condición si se cumple que m==2
    n = int(input("Ingresa un número: "))# ingresamos un numero
    print(" ")
    if n<0:#si el numero es negativo, mencionamos que es invalido
        print("El número ingresado no es válido debe ser positivo")
        m!= 2
        
    div = 0 #iniciamos la variable que va a contar los divisores
    for i in range(1,n+1):#creamos el rango de los divisores que le vamos a revisar a n
        if n % i == 0:
            div= div +1# por cada (i) por la que se pueda dividir la n se aumentara la cantidad total de divisores
    if div>2:# si el total de divisores es mayor que 2 el numero ya no es primo
        print("El numero",(n),"no es primo")
    else:
        print("El número",(n),"es primo")
# Si el numero ingresado en (m) no es ni 1, ni 2 entonces la operación no es valida
else:
    print("La operación indicada no es valida")