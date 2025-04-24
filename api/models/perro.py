from api.models.animal import Animal



class Perro(Animal):

    def __init__(self, nombre: str, raza: str, edad: int, peso: float):
        super().__init__(nombre, edad, peso)  # Propiedades que hereda de padre
        self.__raza = raza

    def get_raza(self):
        return self.__raza

    def set_raza(self, nueva_raza):
        self.__raza = nueva_raza

    def emitir_sonido(self):
        return "Guau, Guau!"
