print("ingresa un numero para comprobar si éste es palindromo o no: ")
n= int(input("numero: "))#Ingresa un número el cual pasará a ser verificado si es un un palindromo
print(" ")#Para que se vea más ordenado
numero=""#Se inicia la variable que se va a imprimir

if n<0:# Vamos a colocar acá una condicion para ver todo negativo como su inverso aditivo y no tener errores
    n=n*-1 

cadena= str(n) #La variable cadena sera el (str) de el entero (n) ingresado

for i in cadena:# Se crea un for para leer la cadena (cadena)
    numero= i + numero #se almacena la (i) en la variable numero en este caso de atrás hacia adelante

if int(numero)==n:#se verifica si el numero es capicúa comparando el entero de la variable con el (n) inicial
    print("El numero ingresado (",(n), ") SI es capicúa")#si el número "numero" es igual a (n) imprime que es capicúa"
    print(" ")# para que se vea mas ordenado
else:
    print("El número ingresado (",(n), ") NO es capicúa")#si el número "numero" es diferente a (n) imprime que es capicúa"
    print(" ")# para que se vea mas ordenado
    