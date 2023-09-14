# Concatenamos listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1+lista2 # Concatenamos
print(lista3)

lista3.extend([7,8,9]) # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5)) # función para ubicar en que indice esta el valor ingresado

# Como saber cuantos valores repetidos hay en una lista
print(lista3.count(1))

# Para poner nuestra lista al reves
lista3.reverse()
print(lista3)

# Para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Métodos de Ordenamiento
lista3.sort()
print(lista3) # Ordena ascendentemente los elementos
lista3.sort(reverse=True) # Ordena descendentemente
print(lista3)

# Repaso tuplas
tupla = (4,'Hola', 3.14, [1, 2, 3], 4, 'Hola') # Puede tener diferentes tipos de elemento
print(tupla)

print(4 in tupla) # Acción booleana, su respuesta es del tipo booleana
# Podemos usar index, count, len
# En tuplas se puede convertir

