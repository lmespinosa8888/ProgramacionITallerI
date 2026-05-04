from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def hacer_sonido(self):
        pass



class Perro(Animal):
    def hacer_sonido(self):
        print("El perro dice: Guau")


# Clase Gato
class Gato(Animal):
    def hacer_sonido(self):
        print("El gato dice: Miau")


# Crear objetos
perro1 = Perro()
gato1 = Gato()


lista_animales = [perro1, gato1]


for animal in lista_animales:
    animal.hacer_sonido()