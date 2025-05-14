"""Un número es un cuadrado perfecto si su raíz cuadrada es un número exacto (sin decimales). Por ejemplo,
el 4 es un cuadrado perfecto (2²), al igual que lo son el 36 (6²) y el 3.500.641 (1871²).
Todos los números que no son cuadrados perfectos pueden multiplicarse por otros para conseguir serlo. Por
ejemplo, el número 8 no es un cuadrado perfecto, pero al multiplicarlo por 2 se obtiene el 16, que sí lo es.

Entradas del programa: La entrada comienza con un número que indica cuántos casos de prueba tendrán que
procesarse. Cada caso de prueba consiste en un número mayor que 0 y menor que 231.
Salidas: Para cada caso de prueba, el programa escribirá por la salida estándar, en una línea independiente, el
número más pequeño que al ser multiplicado por el número del caso de prueba da como resultado un
cuadrado perfecto. """

#Número de casos
print("Todos los números que no son cuadrados perfectos pueden multiplicarse por otros para conseguir serlo")
n = int(input("Cúantos casos desea comprobar: "))
#número de casos
for i in range(0, n):
    m = int(input("ingresa un número mayor que 0 y menor que 2^31: "))
    # establecemos el rango
    if 0<m<(2**31):
        #comprobamos primero si es cuadrado perfecto
        if m**(1/2) - (int(m**(1/2))) == 0:
            print("El número es un cuadrado perfecto")
        else:
            #hallamos el numero mas pequeño o igual
            for j in range(1,m+1):
                if (j*m)**(1/2) - (int((j*m)**(1/2))) == 0:
                    print(f"El numero más pequeño que al multiplicar a {m} da un cuadrado perfecto es: {j}")
                    break       
    else: 
        print("Él número no se encuentra en el rango") 
    