class Rectangulo:
    """
    Crear una clase llamada Rectángulo, debe tenér atributos: altura y base
    el nombre del método será calcular área utilizando la formula:
    área = base * altura. Pero la base y la altura deben ser ingresadas por
    el usuario y los objetos deben ser tres.
    """

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = int(input('Digite el número para la base del rectángulo: '))
altura = int(input('Digite el número para la altura del rectángulo: '))

rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectángulo es: {rectangulo1.calcular_area()}')
