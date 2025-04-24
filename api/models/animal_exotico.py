from api.models.animal import Animal

class Animal_Exotico(Animal):

    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuesto: float):
        super().__init__(nombre, edad, peso)
        self._pais_origen = pais_origen
        self._impuesto = impuesto

    def calcular_flete(self):
        return round(self._peso*self._impuesto, 2)

    def pais_origen(self):
        return self._pais_origen

    def get_impuesto(self):
        return self._impuesto

    def set_pais_origen(self, nuevo_pais_origen):
        self._pais_origen = nuevo_pais_origen

    def set_impuesto(self, nuevo_impuesto):
        self._impuesto = nuevo_impuesto
