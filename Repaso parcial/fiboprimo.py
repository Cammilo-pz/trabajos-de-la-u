n = int(input("ingresa un numero"))
x=n
m=""
a=0
b=1
div=0
if n==1:
    m= m + str(a)
    print(m)
elif n==2:
    m= m + str(a)+","+str(b)
    print(m)
elif n>2:
    m= m + str(a)
    for i in range(2,n+1):
        div=0
        suma = a + b
        a=b
        b=suma
        for l in range(1,i+1):
            if i%l==0:
                div=div +1
        if div==2:
            m= m +"," + str(a)
    print(m)
        
           