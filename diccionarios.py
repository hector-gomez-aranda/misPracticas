diccionarios = {"Huevos": 22.50, "Jamon": 23}
# Cada llave del diccionario es unica, si tratamos de usar la misma se actualizara el valor que tenia
print(diccionarios['Huevos'])

print("Las llaves del diccionar son: ", diccionarios.keys())

print("Los valores del diccionarios", diccionarios.values())

diccionarios.pop("Huevos")  # eliminar la llave Huevos
print(diccionarios)

diccionarios.update({"Leche": 19})  # Añadir la llave leche y valor 19
print(diccionarios)
