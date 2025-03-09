palabra = input("ingresa una palabra")
n = len(palabra)
piglatín = ""
for i in range (n):
    if i == 0:
        pal = palabra[i]
    else:
        piglatín = piglatín + palabra[i]
        
print(piglatín + pal + "ay")