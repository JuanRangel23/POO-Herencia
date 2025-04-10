#Crear un sistema para una escuelea. En este sistema, vamos a tener dos clases principales: Persona y Estudiante. La clase Persona
#tendra dos atributos: nombre y edad, y un metodo que imprimira el nombre y la edad de la persona. La clase Estudiante heredara de la clase
#Persona y tambien tendra un atributo adicional: grado y un metodo que imprimira el grado del estudiante.
#Deberas ultilizar super en el metodo de inicializacion (__init_) para reutilizar el codigo de la clase padre (Persona). 
#Luego crea una instacia de la clase Estudiante e imprime sus atributos y ultiliza sus metodos para asegurarte de que todo funcione correctamente

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def MostrarInfo(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad} años")
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        Persona.__init__(self, nombre, edad)
        self.curso = curso
    def MostrarInfo(self):
       super().MostrarInfo()
       print(f"Grado: {self.curso}")

estudiante = Estudiante("Juan", 25, "5B")

estudiante.MostrarInfo()
