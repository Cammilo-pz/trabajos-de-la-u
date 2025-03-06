n = int(input( "termins: "))
suma = 0
for i in range(n):
    suma = suma + (-1)**i / (2 * i + 1)

print(4*suma)
