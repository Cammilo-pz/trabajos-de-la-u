n = int(input(" ingresa un número:"))# se ingresa un numero
if n**(1/2) - int(n**(1/2)) == 0: #se saca raiz cuadrada de un numero y a esta se le resta la raiz cuadrada entera
    print("el numero ingresado tiene por raiz entera ", (n**(1/2)))# si la resta da 0, es el cuadrado de un numero
else:
    print("el numero ingresado no tiene raiz cuadrada entera")# si no da 0 no es el cuadrado de otro