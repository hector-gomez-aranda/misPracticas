lista = []

lista2 = ["hola", 1, 10]

lista3 = [[1,2,3],"adios"]
#
lista4 = [[1,2,3],[3,4,[7,8]],[3,4,5]]

#print(lista4[1][2][1]) # estos son coordenadas y estamos accediendo lasegundo elemento de la lista y al numero 4

# for x in lista4:
#     print(x)
#     for y in x:
#         print(y)
listaNombres = []
for nombres in range(0,5):
    listaNombres.append(input(f"Ingrese un nombre{nombres+1}: "))

print(listaNombres)

#lista.append("elemento")
''' en vez de hacer esto
for elementolista2 in lista2:
    lista.append(elementolista2)
'''
lista.extend(lista2)

#print(lista)
