n = int(input("Ingrese un numero: "))
m= ""
o= ""
a=0
b=1
for i in range(1,n+1):
    m= m +str(a)+ ","
    if i%2!=0:
        o= o+str(a)+"," 
    suma = a+ b
    a= b
    b= suma
print(m)
print(o)