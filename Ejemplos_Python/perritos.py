class Dog:
    familia = 'preciosos canes' #atributo de clase

    def __init__(self, name):
        self.name = name #atributo de instancia

    d = Dog('Fido')
    e = Dog('Buddy')

    d.familia #compartido por todo perro
    e.familia #compartido por todo perro
    d.name
    e.name
