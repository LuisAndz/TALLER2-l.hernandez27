from api.models.animal_exotico import Animal_Exotico

class Huron(Animal_Exotico):

    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuesto: float):
        super().__init__(nombre, edad, peso, pais_origen, impuesto)

    def emitir_sonido(self):
        return "¡Eek Eek!"

