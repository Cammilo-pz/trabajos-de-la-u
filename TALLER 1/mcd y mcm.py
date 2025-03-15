n1= int(input("Ingrese un número para el primer valor: "))
n2= int(input("Ingrese un número para el segundo valor: "))
if n1%2 == 0 and n2%2 == 0:
    if n1 < n2:
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
    print(mcd)
elif n1%2 != 0 and n2%2 != 0:
        if n1 < n2:
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
        print(mcd)
else: 
        if n1 != n2:
            if n1 > n2:
                max = n1
            else:
                max = n2
            for i in range(n1 * n2, max - 1, -1):
                if i % n1 == 0 and i % n2 == 0:
                    mcm = i
            print(mcm)
        else:
            mcm = n1
 
 
 

