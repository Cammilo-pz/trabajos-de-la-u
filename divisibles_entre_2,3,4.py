# Definimos los valores obtenidos por los sensores, los cuales son automáticos pero en éste caso añadiremos unos manueles
temp = 22 #int(input("Temperatura ambiente:"))
CO2 = 800 #int(input("Concentración de CO2:"))
hum = 50 #int(input("Humedad relativa:"))

#Tenemos que normalizar las variables teniendo en cuenta valores máximos y mínimos de cada unidad
n = (temp - 16) / (30 - 16)
m = (CO2- 400) / (2000 - 400)
l = (hum - 20) / (90 - 20)
#Para que todas las variables estén en la misma escala y se puedan comparar y usar en el sistema de ecuaciones.
print
#Añadimos los coeficientes del sistema de ecuaciones
A = [10,3,2,n*10]
B = [2,10,3, m*10]
C = [3,2,10,l*10]
print(A), print(B), print(C)
print(" ")

A1 = [A[0]/10, A[1]/10, A[2]/10, A[3]/10]
B1 = [B[0]-(2*A1[0]), B[1]-(2*A1[1]), B[2]-(2*A1[2]), B[3]-(2*A1[3])]
C1 = [C[0]-(3*A1[0]), C[1]-(3*A1[1]), C[2]-(3*A1[2]), C[3]-(3*A1[3])]
print(A1), print(B1), print(C1)
print(" ")

B2 = [B1[0]*5/47, B1[1]*5/47, B1[2]*5/47, B1[3]*5/47]
A2 = [A1[0]-(3/10*B2[0]), A1[1]-(3/10*B2[1]), A1[2]-(3/10*B2[2]), A1[3]-(3/10*B2[3])]
C2 = [C1[0]-(11/10*B2[0]), C1[1]-(11/10*B2[1]), C1[2]-(11/10*B2[2]), C1[3]-(11/10*B2[3])]
print(A2), print(B2), print(C2)
print(" ")

C3 = [C2[0]*94/855, C2[1]*94/855, C2[2]*94/855, C2[3]*94/855]
print(C3)
A3 = [A2[0]-(11/94*C3[0]), A2[1]-(11/94*C3[1]), 11/94-(11/94*C3[2]), A2[3]-(11/94*C3[3])]
B3 = [B2[0]-(13/47*C3[0]), B2[1]-(13/47*C3[1]), B2[2]-(13/47*C3[2]), B2[3]-(13/47*C3[3])]

print(A3), print(B3), print(C3)
print(" ")
