#Crear un isstema para una clinica veterinaria. Tendremos dos clases principales: Animales y Perro. La clase Animal tendra los atributos
#nombre y especie, y un metodo que imprimira el nombre y la especie del animal. La clase Perro heredara de la clase Animal y tendra un atribito
#adicional: raza, junto con un metodo que imprimira la raza del perro.
#Deberas ultilizar super en el metodo de inicializacion (__init_) para reutilizar el codigo de la clase padre (Animal). 
#Luego crea una instacia de la clase Perro e imprime sus atributos y ultiliza sus metodos para asegurarte de que todo funcione correctamente

#creacion de la clase padre Animal
class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
 
#creacion del metodoa mostrar informacion   
    def MostrarInfo(self):
        print(f"Nombre: {self.nombre}\nEspecie: {self.especie}")

#creacion de la clase hija Perro quien esta heredando de la ce padre los atributos nombre y especie   
class Perro(Animal):
    def __init__(self, nombre, especie, raza):
        Animal.__init__(self, nombre, especie)
        self.raza = raza

    def MostrarInfo(self):
       super().MostrarInfo()
       print(f"Raza: {self.raza}")

#crear el objeto mascota
mascota = Perro("Cannel", "Canino", "Husky Siberiano")

mascota.MostrarInfo()
