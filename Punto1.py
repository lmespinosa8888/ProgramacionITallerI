# Constructor de clase.
class Vehiculo:
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year

# Metodo para obtener la descripción del vehiculo.

    def descripcion(self):
        return f"El vehiculo es de marca {self.marca} modelo {self.modelo} del año {self.year}"

# Crear varios objetos Vehiculos

Vehiculo1 = Vehiculo ("HONDA", "HV-R", 2025)
Vehiculo2 = Vehiculo ("RENAULT", "ARKANA", 2026)

# Mostrar la descripción del Libro.

print(Vehiculo1.descripcion())
print(Vehiculo2.descripcion())

