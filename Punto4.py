
class Vehiculo:
    def __init__(self, velocidad):
        self.velocidad = velocidad

    def acelerar(self):
        self.velocidad = self.velocidad + 10
        print("El vehículo aceleró. Velocidad actual:", self.velocidad, "km/h")


class Coche(Vehiculo):
    def __init__(self, velocidad, marca):
        super().__init__(velocidad)
        self.marca = marca

    def mostrar_info(self):
        print("Coche marca:", self.marca)
        print("Velocidad:", self.velocidad, "km/h")


class Bicicleta(Vehiculo):
    def __init__(self, velocidad, tipo):
        super().__init__(velocidad)
        self.tipo = tipo

    def mostrar_info(self):
        print("Bicicleta tipo:", self.tipo)
        print("Velocidad:", self.velocidad, "km/h")


# Crear objetos.
coche1 = Coche(20, "Toyota")
bicicleta1 = Bicicleta(5, "Montaña")

print("Información del coche:")
coche1.mostrar_info()
coche1.acelerar()

print()

print("Información de la bicicleta:")
bicicleta1.mostrar_info()
bicicleta1.acelerar()