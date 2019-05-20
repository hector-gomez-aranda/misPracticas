# Operaciones artimeticas
operacion = 90-45*5

#Imprimir en pantalla
print("El resultado es: ")
print(operacion)

#Ingresar datos
nombre = input("Ingresar su nombre por favor: ")
edad = int(input("Ingrese la edad: "))

print(f"Su nombre es: {nombre} y su edad es mas 10 años es  {edad + 10}")

print("Su nombre es: ", nombre, "y su edad", edad) #esta seria la forma normal de hacerlo en python, la coma aqui es para separar mensajes no para concatenarlos

#Condicionales
'''
if condicion: si la condicion es verdadera
    ejecutar codigo
elif condicion: si la condicion anterior es falsa, ejecutar esta condicional
    ejecutar codigo
else: si ninguna de las anteriores es verdadera, ejecutar else
'''
numero = 10

if (numero%2==0 and numero%2==0):
    print("el numero es multiplo de 2")
elif (numero%3==0):
    print("el numero es multiplo de 3")
else:
    print("el numero no es multiplo de 2 ni multiplo de 3")

#Ciclos
while(numero>6):
    print(numero)
    numero-=1

lista = [1,2,3]
for x in range(0, len(lista),1):
    print(lista[x]) #esta es una mala practica de recorrer una lista en un for
    
for elemento in lista:
    print(elemento) # el mejor es este
