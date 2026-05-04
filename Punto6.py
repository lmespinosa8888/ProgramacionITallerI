
class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad = self.velocidad + 10
        print("Vehículo acelera a:", self.velocidad, "km/h")


class Coche(Vehiculo):
    def __init__(self, velocidad, marca):
        super().__init__(velocidad)
        self.marca = marca

    def acelerar(self):
        self.velocidad = self.velocidad + 20
        print("Coche", self.marca, "acelera a:", self.velocidad, "km/h")


class Bicicleta(Vehiculo):
    def __init__(self, velocidad, tipo):
        super().__init__(velocidad)
        self.tipo = tipo

    def acelerar(self):
        self.velocidad = self.velocidad + 5
        print("Bicicleta", self.tipo, "acelera a:", self.velocidad, "km/h")



# Crear objetos.
coche1 = Coche(20, "Mazda")
coche2 = Coche(30, "Toyota")

bici1 = Bicicleta(10, "Montaña")
bici2 = Bicicleta(5, "Ruta")


lista_vehiculos = [coche1, coche2, bici1, bici2]


for vehiculo in lista_vehiculos:
    vehiculo.acelerar()