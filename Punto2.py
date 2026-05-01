class Vehiculo:
    def __init__(self, marca, modelo, year):
        self._marca = marca
        self._modelo = modelo
        self._year = year

    def descripcion(self):
        return f"El vehiculo es de marca {self._marca} modelo {self._modelo} del año {self._year}"
    
    # GET y SET de marca

    def get_marca(self):
        return self._marca

    def set_marca(self, editar_marca):
        if editar_marca != "":
            self._marca = editar_marca

# GET y SET de modelo

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, editar_modelo):
        if editar_modelo != "":
            self._modelo = editar_modelo

# GET y SET de year

    def get_year(self):
        return self._year

    def set_year(self, editar_year):
        if isinstance(editar_year, int):
            self._year = editar_year

# Crear varios objetos Vehiculos

vehiculo1 = Vehiculo("HONDA", "HV-R", 2025)
vehiculo2 = Vehiculo("RENAULT", "ARKANA", 2026)

# Mostrar la descripción del vehiculo.

print(vehiculo1.descripcion())
vehiculo1.set_marca("SUBARU")
vehiculo1.set_modelo("WRX")
vehiculo1.set_year(2027)
print(vehiculo1.descripcion())
print(vehiculo2.descripcion())