# Crear excepción personalizada
class ExcesoVelocidadException(Exception):
    pass


class Coche:
    def __init__(self, marca, velocidad):
        self.marca = marca
        self.velocidad = velocidad

    def incrementar_velocidad(self, aumento):
        nueva_velocidad = self.velocidad + aumento

        # Validar límite
        if nueva_velocidad > 200:
            raise ExcesoVelocidadException("¡Exceso de velocidad!")

        self.velocidad = nueva_velocidad
        print("Velocidad actual:", self.velocidad, "km/h")


# Crear objetos 

coche1 = Coche("Toyota", 180)

try:
    coche1.incrementar_velocidad(10)
    coche1.incrementar_velocidad(20)
except ExcesoVelocidadException as e:
    print("Error:", e)