# Ejercicio 9: Mostar una frase sin espacios y contar su longitud
# Hacer un programa donde el usuario ingrese una frase, se le
# devolverá la misma frase, pero son espacios en blanco, y
# ádemas un contador de cúantos caracteres tiene la frase
# (sin contar los espacios en blanco)
# Ejemplo:      frase = vivir por siempre en paz
#               frase final = vivirporsiempreenpaz
#               n.º de caracteres = 20
frase1 = input('Digite una frase: ')
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'\nFrase final: {frase1}')
print(f'N.° de caracteres: {len(frase1)-1}')
