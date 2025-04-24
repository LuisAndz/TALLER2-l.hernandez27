from abc import ABC, abstractmethod
# Se utiliza para crear una clasepadre


#class Animal(ABC): ---Cambia a heredar los metodos abstractos de iAnimal
class Animal(ABC):

    def __init__(self, nombre: str, edad: int, peso: float):
        # Para ser heredadas se declaran como Privated
        self._nombre = nombre
        self._edad = edad
        self._peso = peso
        
    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_peso(self):
        return self._peso

    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def set_edad(self, nueva_edad):
        self._edad = nueva_edad

    def set_peso(self, nuevo_peso):
        self._peso = nuevo_peso
        
    @abstractmethod
    def emitir_sonido():
        pass
