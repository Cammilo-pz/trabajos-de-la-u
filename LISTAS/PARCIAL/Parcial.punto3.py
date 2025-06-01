#defino la función
def convertir_frase(frase):
    palabras = frase.split()            
    #divide la frase en palabras
    mayuscula = []          
    #lista de palabras separadas
    for i in palabras:                  
        #bucle para convertir la primera letra de cada palabra en mayuscula
            convertida = primera_mayuscula(i)           
            mayuscula.append(convertida)
            respuesta = ' '.join(mayuscula)          
            #une las palabras ya convertidas mediante el join
    return respuesta

def primera_mayuscula(palabra):
    # Convierte la primera letra en mayúscula y une con el resto en minúscula
    palabra = palabra[0].upper() + palabra[1:]
    return palabra
frase = input("Ingrese una frase: ")                            
#solicita la frase al ususario
frase_convertida = convertir_frase(frase)                       

#llama a la función
print("Frase convertida:", frase_convertida)                  
#imprime la frase final