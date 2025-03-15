n = int(input("ingresa un numero:"))# ingresamos un numero inicial 
x = n # x es igual al numero primo que se necesita imprimir
div = 3 # div es la cantidad de divisores que tiene un número, pero lo iniciamos con 3 para que entre al while
if n > 2:
    while div > 2:
        div = 0 # lo iniciamos en 0
        for i in range(1,x+1):
            if x % i == 0:
                div= div +1 # de por si, todo numero tiene 2 divisores básicos, el número y él mismo, pero si no es primo tendrá mas
        if div>2:
            x=x-1
    print("El primo más cercano es:",x)#si tiene dos divisores será el primo cercano menor
else :
    print("ingrese un número mayor a 2")
