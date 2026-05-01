class Vehiculo:
    def __init__(self, marca, modelo, year):
        self._marca = None
        self._modelo = None
        self._year = None

        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_year(year)

    def get_marca(self):
        return self._marca

    def set_marca(self, editar_marca):
        if isinstance(editar_marca, str) and editar_marca.strip() != "":
            self._marca = editar_marca
        else:
            print("Error: La marca debe ser texto y no debe estar vacía")

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, editar_modelo):
        if isinstance(editar_modelo, str) and editar_modelo.strip() != "":
            self._modelo = editar_modelo
        else:
            print("Error: El modelo debe ser texto y no debe estar vacío")

    def get_year(self):
        return self._year

    def set_year(self, editar_year):
        if editar_year is None or editar_year == "":
            print("Error: No puede estar vacío")
            return

        if not isinstance(editar_year, int):
            print("Error: Debe ser número")
            return

        if not 1990 <= editar_year <= 2100:
            print("Error: No puede ser inferior a 1990 ni mayor al 2100")
            return

        self._year = editar_year

    def descripcion(self):
        return f"El vehículo es de marca {self._marca}, modelo {self._modelo} del año {self._year}"

# Lista de objetos

vehiculos = []

# Agregar a la lista de objetos Vehiculos

vehiculos.append(Vehiculo("HONDA", "HV-R", 2027))
vehiculos.append(Vehiculo("MAZDA", "CX5", 2026))
vehiculos.append(Vehiculo("TOYOTA", "4RUNNER", 2025))
vehiculos.append(Vehiculo("SUBARU", "FORESTER", 2024))
#vehiculos.append(Vehiculo("KIA", "K4", "2023"))
#vehiculos.append(Vehiculo("HYUNDAI", "TUCSON", 1890))
#vehiculos.append(Vehiculo("CHEVROLET", "ONIX", 2200))
#vehiculos.append(Vehiculo("FOTON", "TULAND G9","" ))
#vehiculos.append(Vehiculo(678, "QX50", 2022))
#vehiculos.append(Vehiculo("", "Argo", 2021))

# Mostrar la lista de vehiculos.
for v in vehiculos:
    print(v.descripcion())