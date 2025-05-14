n = str(input("ingresa la frase que deseees convertir a cifrado Cesar: "))
print(n)
m = []
palabras = ""
#Almacenamos las palabras de la frase en la lista m
for i in n:
    if i == " ":
        m.append(palabras)
        palabras = ""
    
    else:
        palabras = palabras + i
        
if palabras != "":
    m.append(palabras)    
print(m)
palabra_cifrada = ""
cifrado_cesar = []
for i, p in enumerate(m):
    cesar= ""
    if i%2==0:
        for j in p:
            cifrado = ord(j)
            if 65<=cifrado<=90 or 97<=cifrado<=122:
                cifrado += 4
                if 90<=cifrado<=93:
                    cifrado -= 26
                elif cifrado>=123:
                    cifrado -= 26
            else: cifrado = cifrado    
            cesar= chr(cifrado)
            palabra_cifrada += cesar
        palabra_cifrada += " "
    elif i%2!=0:
        for j in p:
            cifrado = ord(j)
            if 65<=cifrado<=90 or 97<=cifrado<=122:
                cifrado += 3
                if 90<=cifrado<=93:
                    cifrado -= 26
                elif cifrado>=123:
                    cifrado -= 26
            else: cifrado = cifrado 
            cesar= chr(cifrado)
            palabra_cifrada += cesar
        palabra_cifrada += " "        
print(palabra_cifrada)            
            
