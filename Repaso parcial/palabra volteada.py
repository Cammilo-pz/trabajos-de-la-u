print("que desea realizar?:")
print("tiene dos opciones, escoge una colocando el numero 1 o 2")
print("#1 espejo")
print("#2 leer hacia atrás por palabras")
n = int(input())
print("escribe una frase")
m= (input())
x=""
if n == 1:
    for i in m:
        x= str(i)+x
print(x)
h= ""
j= len(m)
if n == 2:
    for i in range(j-1,-1,-1):
        x = m[i]+ x 
        if m[i]==(" "):
            h=h + str(x)
            x=""
    h=h+" " + str(x)
    print(str(h))