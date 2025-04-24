from api.models.animal_exotico import Animal_Exotico


class Boa_Constrictor(Animal_Exotico):

    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuesto: float):
        super().__init__(nombre, edad, peso, pais_origen, impuesto)
        self.__ratones_comidos = 0

    def emitir_sonido(self):
        return "¡Tsss!"

    def comer_raton(self):
        if self.ratones_comidos() == 20:
            raise ValueError("Demasiados Ratones!")

        self.__ratones_comidos += 1

    def ratones_comidos(self):
        return self.__ratones_comidos
