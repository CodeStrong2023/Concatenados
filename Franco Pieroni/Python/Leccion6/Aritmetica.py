class Aritmetica:
    """
    El nombe de este tipo de comentario: DocString
    esto es documentación de la clase en python
    vamos a hacer en esta clase algunas opraciones de: suma, resta, multiplicación y más
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    # Método para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7, 9) # Le pasamos los argumentos para los operandos
print(f'La suma de los números es {aritmetica1.sumar()}')
print(f'La resta de los números es {aritmetica1.restar()}')
print(f'La multiplicación de los números es {aritmetica1.multiplicar()}')
print(f'La división de los números es {aritmetica1.dividir(): .2f}')

