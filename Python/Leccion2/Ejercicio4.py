# Ejercicio Etapas de vida ségun la edad
edad = int(input('Digite su edad: '))
mensaje = None
if 0 <= edad < 10: #Sintaxis simplificada
    mensaje = 'La ifancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios, mucho que estudiar'
elif 20 <= edad < 30:
    mensaje = 'Amor y comienza el trabajo'
elif 30 <= edad < 40:
    mensaje = 'Seguir trabajando y mejorando todos los aspectos de la vida'
    #Debes agregar para las demas edades
else:
    mensaje = 'Error, etapa de vida no renocida'
print(f'Tu edad es: {edad}, {mensaje}')
