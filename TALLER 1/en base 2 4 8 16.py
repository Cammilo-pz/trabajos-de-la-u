n = int(input("ingrese un numero:")) #Ingresa un numero cualquiera
print("escoja una de las siguientes bases:")
print("2, 4, 8 o 16:")
#se escoge cualquiera de las bases posibles
b = int (input())
#inicializa la variable factor 
factor = 1
#inicializa la variable que se va a imprimir para bases 2 4 8
m=0
#Incializa la variable a imprimir para base 16
hexadecimal=""
# condición para numero en base
if b==2 or b==4 or b==8:
    # bucle mientras
    while n>0:
        r = n % b #residuo
        n = n // b #división entera
        m = m + factor * r #numero en base
        factor = factor * 10 #valor posicional de un numero   
    print(m)  
elif b == 16:
        while n>0:
            r = n % b #residuo
            if r<10: #se agregan las letras hexadecimales 
                hexadecimal = str(r) + hexadecimal
            elif r == 10:
                hexadecimal = "A" + hexadecimal  
            elif r == 11:
                hexadecimal = "B" + hexadecimal  
            elif r == 12:
                hexadecimal = "C" + hexadecimal  
            elif r == 13:
                hexadecimal = "D" + hexadecimal  
            elif r == 14:
                hexadecimal = "E" + hexadecimal  
            elif r == 15:
                hexadecimal = "F" + hexadecimal  
            n = n // b   #se hace la división entera hasta que se llegue a 0
        print(hexadecimal) # se imprime la variable que contiene los numeros o letras
else:
    print ("Base invalida")    

    


  
    


