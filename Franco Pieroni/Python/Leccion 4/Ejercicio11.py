# Ejercicio 11: Agenda Telefónica
# Hacer un programa que simule una agenda de contactos. Crear un
# diccionario donde la clave sea el nombre del usuario y el valor
# sea el telefono, el programa tendrá el siguiente menú de opciónes:
#        1. Nuevo contacto
#        2. Borrar contacto
#        3. Ver contactos existentes
#        4. Salir

agenda = {

}
opcion = 0


def menu():
    print("              .:MENÚ:.")
    print("         1. Nuevo contacto")
    print("         2. Borrar contacto")
    print("         3. Ver contactos existentes")
    print("         4. Salir\n")



while True:

    menu()
    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        nombre = input("Ingrese un nombre: ")
        tel = int(input("Ingrese un número de telefono: "))
        if nombre not in agenda:
            agenda[nombre] = tel
            print("Contacto agregado exitosamente!\n")
        else:
            print("Este nombre de contacto ya existe\n")
    elif opcion == 2:
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del (agenda[nombre])
            print("Eliminado exitosamente!\n")
        else:
            print("Este contacto no existe ne la agenda\n")

    elif opcion == 3:

        print("Agenda de contactos")
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}, Teléfono: {valor}')
            print("")

    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos\n")
        break
    else:
        print("Ingrese una opción válida(!)\n")