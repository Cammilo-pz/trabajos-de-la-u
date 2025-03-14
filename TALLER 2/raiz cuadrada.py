n = int(input(" ingresa un número:"))
if n**(1/2) - int(n**(1/2)) == 0:
    print("el numero ingresado tiene por raiz entera ", (n**(1/2)))
else:
    print("el numero ingresado no tiene raiz cuadrada entera")