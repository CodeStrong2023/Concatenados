"""
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los alumnos de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben x128, la variable y = x872, la variable z = x192
print(id(y))
print(id(z))

# Tipos int, float, String, Bool
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola Alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (String)
miGrupoFavorito = "The Neighbourhood"+" "+"The Best Band i Heard"
caracteristicas = "The Best group"
print("Mi grupo favorito es:", miGrupoFavorito, caracteristicas)

numero1 = "7"
numero2 = "8"
print(int(numero1) + int(numero2))

# Tipos Booleanos (bool)

miBooleano = 3 > 2
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
# funcion input
# resultado = input("Digite un numero: ")  # regresa un dato tipo String
# print(resultado)

# Conversion de la  entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 =int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)
"""
"""
operandoA = 8
operandoB = 5
suma = operandoA + operandoB
 #print("Resultado de la suma: ", suma)
print(f"El resultado de la suma es: {suma}")

resta =operandoA - operandoB
print(f"El resultado de la suma es: {resta}")

multiplicación = operandoA * operandoB
print(f"El resultado de la multiplicación es: {multiplicación}")

división = operandoA / operandoB
print(f"El resultado de la división es: {división}")
división = operandoA // operandoB
print(f"El resultado de la división (int) es: {división}")
modulo = operandoA % operandoB
print(f"El resultado de la división o residuo (modulo) es: {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")
"""
"""
alto = int(input('Proporciona el alto  del rectangulo: '))
ancho = int(input('Proporciona el ancho del rectangulo: '))
area = alto * ancho
perimetro = (alto + ancho) * 2
print('Area: ', area)
print('Perimetro: ', perimetro)
"""
"""
miVariable3 = 10
print(miVariable3)

# Operadores de reasignación
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

# miVariable3 = miVariable3 -2
miVariable3 -= 2
print(miVariable3)

# miVariable3 = miVariable3 *3
miVariable3 *= 3
print(miVariable3)

# miVariable3 = miVariable3 /2
miVariable3 /= 2
print(miVariable3)

# Operadores de Comparación

d = 4
b = 2
resultado = d == b  # Comprobamos si son iguales
print(resultado)

# Operador diferente
resultado = d != b
print(resultado)

# Operador mayor que
resultado = d > b
print(resultado)

# Operador menor que
resultado = d < b
print(resultado)

# Operador menor o igual que
resultado = d <= b
print(resultado)

# Operador mayor o igual que
resultado = d >= b
print(resultado)
"""
"""
a = int(input("Digite un número: "))
print(f"El residuo de la división es: {a % 2}")
if a % 2 == 0:
    print(f"El valor de a es: {a} es un número PAR")
else:
    print(f"El valor de a es: {a} es número IMPAR")
"""
"""
edadAdulto = 18
edadPersona = int(input("Digite su edad: "))

if edadPersona >= edadAdulto:
    print(f"Su edad es: {edadPersona} años, Usted es mayor de edad")
else:
    print(f"Su edad es: {edadPersona} años, Usted es menor de edad")
"""
"""
# Operadores Lógicos

a = False
b = False
resultado = a and b
print(resultado)

# Operador or
resultado = a or b
print(resultado)

# Operador not
resultado = not a
print(resultado)

# Ejercicio: Valor demtro de un rango
valor = int(input("Digite un número dentro del rango 0 al 5: "))
valorMinimo = 0
valorMaximo = 5
dentroRamgo= (valor >= valorMinimo and valor <= valorMaximo)
if dentroRamgo:
    print(f"El valor {valor} esta demtro del rango")
else:
    print(f"El valor {valor} No esta dentro del rango")
"""
"""
# Ejercicio con el operador or
vacaciones = True
diaDescanso = True
if not (vacaciones or diaDescanso):
  print('Tiene trabajo que hacer')
else:
  print('Puede asistir al juego')
"""
"""
# Ejercicio: Rango entre 20 y 30 años
edad = int(input("Digite un número: "))
# veinte = edad >= 20 and edad < 30
# print(veinte)
# treinta = edad >= 30 and edad <40
# print(treinta)

# if veinte or treinta:
if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
 print('Estas dentro del rango de los (20\'0) a (30\'0) años')
#  if veinte:
#    print('Estas dentro del rango de los (20\'0)  años')
#  elif treinta:
#    print('Estas dentro del rango de los  (30\'0) años')
#  else:
#   print("No estas dentro del rango")
else:
 print('No estas dentro del rango de los (20\'0) a (30\'0) años')
"""
"""
numero1 = int(input('Digite el valor para el numero1: '))
numero2 = int(input('Digite el valor para el numero2: '))

if numero1 > numero2:
 print('EL numero 1 es mayor')
else:
 print('El numero 2 es mayor')
"""

# Ejercicio: Tienda de libros
print('Digite los sigientes datos del libro')
nombre = input('Digite el nombre del libro: ')
id = int(input('Digite el ID del libro: '))
precio = float(input('Digite el precio del libro: '))
envioGratuito = input('Indicar  si el envío es gratuito (True/False): ')
if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'El valor es incorrecto, debe escribir True/False'
print(f'''
       Nombre: {nombre}
       Id: {id}
       Precio: {precio}
       Envio Gratuito?: {envioGratuito}
''')
