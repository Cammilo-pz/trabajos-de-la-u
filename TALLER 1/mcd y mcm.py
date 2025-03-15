n1= int(input("Ingrese un número para el primer valor: ")) #primer numero
n2= int(input("Ingrese un número para el segundo valor: ")) #segundo numero
if n1%2 == 0 and n2%2 == 0: # se crea la condición inical de ambos pares
    if n1 < n2: #se verifica el mcd
        for i in range(1, n1 + 1, 1):
            if n1 % i == 0 and n2 % i == 0:
                mcd = i
    else:
        if n1 > n2:
            i = 1
            while i <= n2:
                if n1 % i == 0 and n2 % i == 0:
                    mcd = i
                i = i + 1
        else:
            mcd = n1
    print(("mcd: ") and mcd)
elif n1%2 != 0 and n2%2 != 0: #se crea la condición ambos impares
        if n1 < n2: #se verifica el mcd
            for i in range(1, n1 + 1, 1):
                if n1 % i == 0 and n2 % i == 0:
                    mcd = i
        else:
            if n1 > n2:
                i = 1
                while i <= n2:
                    if n1 % i == 0 and n2 % i == 0:
                        mcd = i
                    i = i + 1
            else:
                mcd = n1
        print(("mcd: ") and mcd)
else: # se genera de por sí la condición par impar o viceversa
        if n1 != n2: #se verifica el mcm
            if n1 > n2:
                max = n1
            else:
                max = n2
            for i in range(n1 * n2, max - 1, -1):
                if i % n1 == 0 and i % n2 == 0:
                    mcm = i
            print(("mcm: ") and mcm)
        else:
            mcm = n1
 
 
 

