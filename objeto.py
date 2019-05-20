class Persona:
    cabello = "negro"
    def __init__(self, edad, peso, nacionalidad, altura): #el self es como el this de java
        # el self se refiere a el mismo, a su objeto mismo, el init es el constructor
        self.edad = edad
        self.peso = peso
        self.nacionalidad = nacionalidad
        self.altura = altura

    def descripcion(self):
        print(self.edad, self.peso, self.nacionalidad, self.altura)

    def sentarse(self):
        print("La persona ejecuta la accion de sentarse")
    def pararse(self):
        print("La persona ejecuta la accion de pararse")

ivan = Persona(23, 88, "mexicana", 1.68)
daniel = Persona(23, 88, "mexicana", 1.68)

# ivan.descripcion()
# daniel.descripcion()
# print(ivan.cabello)
# print(daniel.cabello)
# ivan.edad = 45
# ivan.descripcion()
# ivan.sentarse()
# daniel.pararse()

#Herencia
class Alumno(Persona):
    def __init__(self, nombre, matricula, escuela):
        super().__init__(19,87,"mexicana", 1.80) #acceder a la clase padre
        self.nombre = nombre
        self.matricula = matricula
        self.escuela = escuela

    def descripcion(self):
        print(self.nombre,"tiene:", self.edad, "años, pesa:",self.peso, "kg, estudia en:", self.escuela, "y su matricula es:", self.matricula)
alumno = Alumno("Kenny", "E15081234","ITM")
alumno2 = Alumno("andrea", "F3478","UADY")
#alumno.descripcion()

#Polimorfismo
from math import pi #el import puede ser donde sea, no es como java que tiene que ser arriba
class Figura:
    def __init__(self, nombre_figura, color):
        self.nombre_figura = nombre_figura
        self.color = color
    
    #Un metodo puede ser usado de diferentes formas
    def area(self):
        pass

class CirculoVerde(Figura):
    def __init__(self, nombre ,radio):
        super().__init__(nombre, "Verde")
        self.nombre = nombre #lo esta guardando para el mismo
        self.radio = radio

    def area(self):
        return pi*self.radio**2 #**2 es una potencia

class TrianguloRojo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre, "rojo")
        #el nombre no lo estoy pasando como un parametro para el el self.nombre = nombre
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base*self.altura)/2
    
    def area2(self, base ,altura):
        resultado = (self.base*self.altura)/2
        print(resultado)

    def suma(self, area):
        print(area+10)

circulo = CirculoVerde("circulito", 4)
triangulo = TrianguloRojo("triangulo equilatero", 3, 4)
print(circulo.nombre)
print(triangulo.nombre_figura)
print(circulo.area())
#Metodo con return
print(triangulo.area())
#Metodo con print
triangulo.area2(triangulo.base,triangulo.altura)

#Tener cuidado cuando regreso un valor o cuando imprimo un valor en pantalla

triangulo.suma(triangulo.area())

#triangulo.suma(triangulo.area2(triangulo.base,triangulo.altura))
