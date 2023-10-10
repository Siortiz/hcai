class Persona():
    ""Esta es una clase genérica para para almacenar personas""

    def __init__(self):
        self.items = 0
        self.tlocal = 0 #tiempo total en el super

class Validador(Persona):
    ""Esta es una clase para representar personas que validen items""

    def __init__(self, fac=10):
        # Este es el factor de conversion items a tiempo de validación
        self.validfactor = fac
        self.validationTime = 0

    def get_item(self, nitems):
        self.items = nitems
        self.validationTime = nitems*self.validfactor

    def validar(self, dt):
        while(0 < dt and 0 < self.validationTime):
            self.validationTime -= 1
            dt -= 1
        return dt
class Cliente
        
