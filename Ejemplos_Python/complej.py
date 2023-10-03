class Complex:
    'Otra clase de números complejos'

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        return str(self.r)+'+i'+str(self.i)
    
    def __add__(self, other):
        print(self)
        return Complex(self.r+other.r, self.i+other.i)

    def mostrar(self):
        rep =self.__str__()
        print('Número precioso:'+rep)
