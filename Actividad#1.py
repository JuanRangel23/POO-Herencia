#Crear un sistema para una escuelea. En este sistema, vamos a tener dos clases principales: Persona y Estudiante. La clase Persona
#tendra dos atributos: nombre y edad, y un metodo que imprimira el nombre y la edad de la persona. La clase Estudiante heredara de la clase
#Persona y tambien tendra un atributo adicional: grado y un metodo que imprimira el grado del estudiante.
#Deberas ultilizar super en el metodo de inicializacion (__init_) para reutilizar el codigo de la clase padre (Persona). 
#Luego crea una instacia de la clase Estudiante e imprime sus atributos y ultiliza sus metodos para asegurarte de que todo funcione correctamente

#Creacion de la clase padre persona
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#creacios de metodo para mostrar informacion
    def MostrarInfo(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad} años")
        
#creacion de la clase hija Estudiante
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso): #creacion de atributo de la clase hija
        Persona.__init__(self, nombre, edad)
        self.curso = curso

#creacion de la metodo mostrar informacion que estaheredando de la clase padre
    def MostrarInfo(self):
       super().MostrarInfo()
       print(f"Grado: {self.curso}")

#creacion de objeto
estudiante = Estudiante("Juan", 25, "5B")

estudiante.MostrarInfo()
