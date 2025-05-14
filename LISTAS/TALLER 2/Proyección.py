"""5. Construir un programa que reciba las componentes en x y y de un vector y calcule una proyección del
mismo sobre un par de vectores unitarios al azar. El programa de permitir recibir más de un vector, pero uno
a la vez. Para cada caso graficar el punto inicial y los puntos que representan las proyecciones."""
#Toma de los vectores
import random as rnd 
import matplotlib.pyplot as plt
n = int(input("cuántos vectores desea proyectar?: "))
#ecuación del circulo
Y=[]
X=[]
for _ in range(100):
    numero_aleatorio = rnd.uniform(-1, 1)
    X.append(numero_aleatorio)
for j in range(len(X)):
    Y.append((1-(X[j]**2))**(1/2))
for i in range(0,n):
    print("Ingrese las coordenadas x, y de su vector")
    x = float(input("x = " ))
    y = float(input("y = " ))
    V = [x, y]
    print(f"el vector escogido es: {V}")
    print("los vectores aleatorios son: ")
    for i in range(0,2):
        x1 = rnd.randint(1,10)
        y1 = rnd.randint(1,10)
        #print(x1, y1)
        #convertimos el vector aleatorio a unitario
        norma_u = ((x1**2) + (y1**2))**(1/2)
        U = [x1/norma_u, y1/norma_u]
        print (U)
        x_proyección_U_en_V = ((V[0]*U[0]+V[1]*U[1])/ (norma_u**2)) * U[0]
        y_proyección_U_en_V = ((V[0]*U[0]+V[1]*U[1])/ (norma_u**2)) * U[1]
        
        Proyeccion = [x_proyección_U_en_V, y_proyección_U_en_V]
        
        plt.plot(X, Y, "r_",V[0], V[1], "b*", U[0],U[1], "g*", Proyeccion[0], Proyeccion[1], "m*")
        
plt.show()    




