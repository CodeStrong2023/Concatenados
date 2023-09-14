# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree unalista con los siguientes personajes del señor de los anillos

# Nombre: Aragorn
# Clase: Guerrero
# Raza: Dúnedain del Norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []

P = {'Nombre': 'Aragorn', 'Clase': 'Guerrero', 'Raza': 'Dúnedain del Norte'}
personajes.append(P)
P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)

# Tarea: agregamos tres personajes

P = {'Nombre': 'Gimli', 'Clase': 'Martillo', 'Raza': 'Enano de Erebor'}
personajes.append(P)
P = {'Nombre': 'Boromir', 'Clase': 'Paladin', 'Raza': 'Dúnedain'}
personajes.append(P)
P = {'Nombre': 'Frodo', 'Clase': 'Pícaro', 'Raza': 'Hobbit'}
personajes.append(P)

print(personajes)