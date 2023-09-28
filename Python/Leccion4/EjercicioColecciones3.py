# Ejercicio 3: Agregar personajes a una lista
# Escriba un programa donde cree una lista con los siguientes personajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

# Nombre: Gandalf
# Clase: Mago
# Raza: Istar

# Nombre: Legolas
# Clase: Arquero
# Raza: Elfo Sindar

# Nombre: Gollum
# Clase:
# Raza: Hobbit corrompido

# Nombre: Galadriel
# Clase:
# Raza: Elfos Noldor

# Nombre: Sauron
# Clase: Ainur
# Raza: Maiar (Ainur)

personajes = [] # Creamos una lista vacia
# Creamos diccionarios
P = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dúnadan del norte'}
personajes.append(P) # Agregamos a la lista un personaje
P = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(P)
P = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(P)
P = {'Nombre': 'Gollum', 'Clase': '', 'Raza': ''}
personajes.append(P)
P = {'Nombre': 'Galadriel', 'Clase': '', 'Raza': ''}
personajes.append(P)
P = {'Nombre': 'Sauron', 'Clase': '', 'Raza': ''}
personajes.append(P)
print(personajes) # Tarea: Agregar por lo menos otros tres personajes, que sean a tu elección
