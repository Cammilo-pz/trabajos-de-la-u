inicio = "comienzo"
while inicio == "comienzo":

    # MENU CON LAS POSIBLES OPCIONES
    print("que operación desea realizar? Escriba el signo:")
    print("Suma: +")
    print("Resta: -")
    print("Multiplicación: *")
    print("División: /")
    print("si desea salir coloca: x")
    operacion = input()

    # OPERACIONES CON NÚMEROS DIFERENTES

    if operacion == "+":
        n1 = float(input("numero 1:"))
        n2 = float(input("numero 2:"))
        print(n1 + n2)
    elif operacion == "-":
        n1 = float(input("numero 1:"))
        n2 = float(input("numero 2:"))
        print(n1 - n2)
    elif operacion == "*":
        n1 = float(input("numero 1:"))
        n2 = float(input("numero 2:"))
        print(n1 * n2)
    elif operacion == "/":
        n1 = float(input("numero 1:"))
        n2 = float(input("numero 2:"))
        print(n1 / n2)
    elif operacion == "x":
        inicio == "final"
    

    espacio = input("si desea realizar otra operación dale espacio, enter. Si desea salir escribe x:")
    if espacio == (" "):
        inicio = "comienzo"
    else:
        inicio = "final"
    print(" ")
    print(" ")
    print(" ")