n = int(input("Ingresa un número: "))
numeros= 0
#Ciclo que verifica lola divisibilidad de numeros entre 1 y n
for i in range(1, n + 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        numeros = i
        print (i)
        
        
        
 #De forma ordenada serían  
print("De forma ordenada:")     
numeros  = []
for i in range(1, n+1)
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        numeros.append(i)
print("Números menores que", n, "divisibles entre 2, 3 o 5:", numeros)        