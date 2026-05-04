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

    # Sobreescritura del método acelerar
    def acelerar(self):
        self.velocidad = self.velocidad + 20
        print("El coche acelera más rápido a:", self.velocidad, "km/h")

    def mostrar_info(self):
        print("Coche marca:", self.marca)


class Bicicleta(Vehiculo):
    def __init__(self, velocidad, tipo):
        super().__init__(velocidad)
        self.tipo = tipo

    # Sobreescritura del método acelerar
    def acelerar(self):
        self.velocidad = self.velocidad + 5
        print("La bicicleta acelera más lento a:", self.velocidad, "km/h")

    def mostrar_info(self):
        print("Bicicleta tipo:", self.tipo)


# Crear objetos. 

coche1 = Coche(20, "Toyota")
bicicleta1 = Bicicleta(5, "Montaña")

print("Coche:")
coche1.mostrar_info()
coche1.acelerar()

print()

print("Bicicleta:")
bicicleta1.mostrar_info()
bicicleta1.acelerar()