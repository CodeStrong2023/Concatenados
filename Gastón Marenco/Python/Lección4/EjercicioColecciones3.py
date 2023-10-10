# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos

# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del Norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

personajes = []  # Creamos una lista vacia

# Creamos diccionarios
P = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del Norte'}
personajes.append(P)  # Agregamos al a lista un personaje

P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)

P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)

# Tarea: Agregar por lo menos, otros tres personajes, que sean de tu eleccion
P = {'Nombre': 'Frodo Bolsón', 'Clase': 'Aventurero', 'Raza': 'Hobbit'}
personajes.append(P)
P = {'Nombre': 'Bilbo Bolsón', 'Clase': 'ladrón', 'Raza': 'Hobbit'}
personajes.append(P)
P = {'Nombre': 'Sauron', 'Clase': 'Hechicero', 'Raza': 'Maiar'}
personajes.append(P)

print(personajes)
