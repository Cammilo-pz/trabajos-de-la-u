import random as rnd 

#Cantidad de números con la que se quiere trabajar
n= int(input("Ingresa la cantidad de numeros que desea almacenar en la lista: "))
A= []
#Almacenar numeros en la variable creada anteriormente
for i in range (n):
    A.append(rnd.randint(0,100))
print(A)

#comenzamos a sacar el promedio 
def media(Z):
    media = sum(Z)/len(Z)
    return media

#ahora la mediana
def mediana(Z):
    n = len(Z)
    for j in range(len(Z)):
        for i in range(len(Z)-1):
            if Z[i] > Z[i+1]:
                a = Z[i]
                Z[i] = Z[i+1]
                Z[i+1] = a
    
    print(Z)
    
    # Comprobar si la cantidad de elementos es par
    if n % 2 == 0:
        mediana = Z[int(n/2)-1] 
        mediana = Z[int((n+1)/2)-1] 
    
    return mediana

#* Varianza y Dispersión 
def varianza(Z):
    
    sum = 0
    for i in Z:
        sum = sum + ((i - media(Z))**2)
    varianza = sum / (len(Z) - 1)
    
    return varianza

#Desviación estandar
def desviacion(Z):
    desviacion = varianza(Z)**(1/2)
    
    return desviacion

def rango(Z):
    rango = max(Z) - min(Z)
    
    return rango

# Comprobar que se generaron elementos
if len(A) == 0:
    print("|| ERORR || -- Debes pedir generar al menos 1 elemento")
else:
    
    print(A)
    print(" ")
    print(f"Media: {media(A)}")
    print(" ")
    print(f"Mediana: {mediana(A)}")
    print(" ")
    print(f"Varianza: {varianza(A)}")
    print(" ")
    print(f"Desviación estandar: {desviacion(A)}")
    print(" ")
    print(f"Rango: {rango(A)}")
    print(" ")
    