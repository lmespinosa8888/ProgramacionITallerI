class Motor:
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def mostrar_motor(self):
        print("Motor:", self.tipo, "-", self.potencia, "HP")


class Coche:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def describir(self):
        print("Coche:", self.marca, self.modelo)
        self.motor.mostrar_motor()


# Crear objetos Motor
motor1 = Motor(150, "Gasolina")
motor2 = Motor(100, "Eléctrico")

# Crear objetos Coche con motores
coche1 = Coche("Toyota", "Corolla", motor1)
coche2 = Coche("Tesla", "Model 3", motor2)


lista_coches = [coche1, coche2]


for coche in lista_coches:
    coche.describir()
    print()