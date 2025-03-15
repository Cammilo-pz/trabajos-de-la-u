n = int(input("Ingrese el número hasta el cuál desea revisar divisores:"))
m = ""
Div2 = 2
Div3 = 3
Div5 = 5
for i in range(1, n+1):
    if i%2==0 or i%3==0 or i%5==0:
        m = str(i)+"."+" Divisible por "
        if i%2 == 0:
            m = m + str(Div2)+" "
            if i%3==0 or i%5==0:
                m = m + "y "
        if i%3 == 0:
            m = m + str(Div3)+" "
            if i%5==0:
                m = m + "y "
        if i%5 == 0:
            m = m + str (Div5)+" "
    else:
        m = str(i)+"."
    print(m)
        