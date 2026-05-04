from abc import ABC, abstractmethod

# "Interfaz" Volador
class Volador(ABC):

    @abstractmethod
    def volar(self):
        pass


# Clase Pajaro
class Pajaro(Volador):
    def volar(self):
        print("El pájaro vuela con sus alas")



class Avion(Volador):
    def volar(self):
        print("El avión vuela con motores")


# Crear objetos
pajaro1 = Pajaro()
avion1 = Avion()


lista_voladores = [pajaro1, avion1]


for volador in lista_voladores:
    volador.volar()