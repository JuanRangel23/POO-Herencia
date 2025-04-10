#Crear un sistema de vehiculos. Tendremos dos clases principales: Vehiculo y Coche. La clase Vehiculo tendra los atributos los marca y año.
#y un metodo que imprimiea la marca y el año del vehiculo. La clase Coche heredara de la clase Vehiculo y tendra un atributo adicioal: modelo
#juan con un metodo que imprimira el modelo del coche.
#Deberas ultilizar super en el metodo de inicializacion (__init_) para reutilizar el codigo de la clase padre (Vehiculo). 
#Luego crea una instacia de la clase Choche e imprime sus atributos y ultiliza sus metodos para asegurarte de que todo funcione correctamente

class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año
        
    def MostrarInfo(self):
        print(f"Marca: {self.marca}\nAño: {self.año}")

class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        Vehiculo.__init__(self, marca, año)
        self.modelo = modelo
    
    def MostrarInfo(self):
        super().MostrarInfo()
        print(f"Modelo: {self.modelo}")

carro = Coche("Audi", 2024, "RT34")

carro.MostrarInfo()
