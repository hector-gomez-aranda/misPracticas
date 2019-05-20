#entrada = input("Ingresa algo: ")

#print(entrada)
def elegirPalabra():
    respuesta = ""
    #esto es un set
    diccionario = {"hola", "adios", "entrada","a","b","c","d","e","f","g","h","y","j"}
    for x in range(len(diccionario)):
        for palabra in diccionario:
            respuesta = palabra
    return respuesta

# hola = elegirPalabra()
# print(hola)
