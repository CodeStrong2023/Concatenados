class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos:
    altura y base. El nombre del método será calcular_area utiizando la fórmula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el
    usuario y los objetos deben ser 3
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = int(input('Ingrese la base del rectangulo: '))
altura = int(input('Ingrese la altura del rectangulo: '))

rectangulo1 = Rectangulo(base, altura)
print(f'EL area del rectangulo es: {rectangulo1.calcular_area()}')


