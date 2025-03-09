n = int(input("ingrese un numero:")) 
b= int (input("ingrese una base:"))
factor = 1
m=0
if b>=2 and b<10:
   while n>0:
    r = n % b
    n = n // b
    m = m + factor * r
    factor = factor * 10
else :
    print ("Base invalida")

print(m)    
    


