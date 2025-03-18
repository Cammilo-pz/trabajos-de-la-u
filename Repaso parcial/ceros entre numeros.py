n= int(input("Ingresa un número: "))
x= str(n)
numeros= len(x)
m=""
for i in x:
        n= int(i)*10
        j= str(n)
        m= m + str(n)
m=int(m)/10
print(int(m))

    