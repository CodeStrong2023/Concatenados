from Persona2 import Persona2
print('Creación de Objetos'.center(50, '-'))
if __name__ == '__main__': # Comprobación del método principal de ejecución
    persona5 = Persona2('Franco','Pieroni',29)
    persona5.mostrar_detalles()

    print(__name__)

print('Eliminacion de Objetos'.center(50, '-'))
del persona5