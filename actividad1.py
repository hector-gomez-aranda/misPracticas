#Actividad
#Realizar un programa que pida el nombre de 3 personas, a cada persona se le pedira que ingrese su calificacion(5), 
#sacar promedio de cada persona, desplegar un mensaje con el nombre de la persona y su promedio

alumnos = []
calificaciones = []
aux = []
promedios = []

for x in range(0,3):
    alumnos.append(input("Ingrese su nombre: "))
    for y in range(0,5):
        aux.append(float(input(f"ingresa la {y+1} calificacion: ")))
    calificaciones.append(aux)
    aux = []
b = 0
promedio = 0
for z in calificaciones:
    for x in z:
        promedio +=x
    promedios.append(promedio / 5)
    print("La persona:", alumnos[b], "tiene un promedio de:" ,promedios[b])
    b+=1
    promedio = 0 
# y = 0
# for w in alumnos:
    
#     print("Alumno:",w, "promedio: ", promedios[y])
#     y += 1
