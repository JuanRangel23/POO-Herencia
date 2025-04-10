#Crear un sistema de vehiculos. Tendremos dos clases principales: Vehiculo y Coche. La clase Vehiculo tendra los atributos los marca y año.
#y un metodo que imprimiea la marca y el año del vehiculo. La clase Coche heredara de la clase Vehiculo y tendra un atributo adicioal: modelo
#junto con un metodo que imprimira el modelo del coche.
#Deberas ultilizar super en el metodo de inicializacion (__init_) para reutilizar el codigo de la clase padre (Vehiculo). 
#Luego crea una instacia de la clase Choche e imprime sus atributos y ultiliza sus metodos para asegurarte de que todo funcione correctamente

#creamos la clase vehiculo junto a sus atributos
class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año

#definimos el metdo que imprimira los atributos de la clase
    def MostrarInfo(self):
        print(f"Marca: {self.marca}\nAño: {self.año}")

#creamos la clase hijo choche quien esta heredando de la clase padre vehiculo 
class Coche(Vehiculo):
    def __init__(self, marca, año, modelo): # se añade un atributo propia de la clase hijo
        Vehiculo.__init__(self, marca, año)
        self.modelo = modelo

#definimos el metodo que imprimira en pantalla tanto el metodo padre como el hijo
    def MostrarInfo(self):
        super().MostrarInfo()
        print(f"Modelo: {self.modelo}")

#creamos el objero carro
carro = Coche("Audi", 2024, "RT34")

carro.MostrarInfo()
