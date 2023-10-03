class Complex:
    def __init__(self, r=0, i=0):
        self.i = i
        self.r = r
    def mostrar(self):
        print(str(self.r)+"+ i"+str(self.i))
