n = int(input("Ingrese el número hasta el cuál desea revisar divisores:"))# se ingresa el numero limite
#se inicializan las variables
m = ""
Div2 = 2
Div3 = 3
Div5 = 5
for i in range(1, n+1): #se crea el rango y la condición
    if i%2==0 or i%3==0 or i%5==0:#si es divisible por alguno se procede a revisar entre cuál es divisible
        m = str(i)+"."+" Divisible por "
        if i%2 == 0: #divisible entre 2 
            m = m + str(Div2)+" "
            if i%3==0 or i%5==0:
                m = m + "y " #se agrega una condición que revisa si tendrá mas divisores y agrega una "y"
        if i%3 == 0: #divisible entre 3
            m = m + str(Div3)+" "
            if i%5==0:
                m = m + "y "
        if i%5 == 0: #divisible entre 5
            m = m + str (Div5)+" "
    else:
        m = str(i)+"." #si no es divisible por ninguno unicamente se coloca el numero y el punto
    print(m)# se imprime lo que contenga m
        