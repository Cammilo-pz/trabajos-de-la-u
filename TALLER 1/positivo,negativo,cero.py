n = int(input("ingrese un número: "))
if n == 0:
    print("el número es cero")
elif n>0:
    print("el número es positivo")
else:
    print("el numero es negativo")

i = 1
neg = 0
num_pos = 0
num_neg = 0
pos = 0
print(" ")
print("ingresa la cantidad de numeros positivos negativos que desee")
print("si no desea ingresar más, escriba el numero cero")
while i!=0:
    m = int(input())
    i = m
    if m<0:
        neg= neg + 1
        num_neg = num_neg + m
    elif m>0:
        pos= pos + 1
        num_pos= num_pos + m
    else:
        print(" ")
        print("la cantidad de numeros positivos fue de: "); print(pos)
        print("y su promedio de:");print(num_pos/pos)
        print(" ")
        print("la cantidad de numeros negativos fue de: ");print(neg)
        print("y su promedio de: ");print(num_neg/neg)
        