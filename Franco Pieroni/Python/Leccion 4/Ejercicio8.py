# Ejercicio 8: Menú interactivo - Cajero automático
# Hacer un programa que simule un cajero autamático con un saldo de 1000$
# y tendrá el siguiente menú de opciones:

#                1.Ingresar dinero en la cuenta
#                2.Retirar dinero de la cuenta
#                3.Mostrar dinero disponible
#                4.Salir

saldo = 1000
while True:
    print("\n        \t.:MENÚ:. ")
    print("\n1.Ingresar dinero en la cuenta")
    print("2.Retirar dinero de la cuenta")
    print("3.Mostrar dinero disponible")
    print("4.Salir")
    opcion = int(input("\nIngrese una opción-> "))

    if opcion == 1:
        extra = float(input("\nCuanto dinero desea ingresar-> "))
        saldo += extra
        print(f"\nDinero en la cuenta al momento: ${saldo}")
    elif opcion == 2:
        extra = float(input("\nCuanto dinero desea retirar-> "))
        while extra > saldo:
            print("\nSaldo insuficiente(!)")
            extra = float(input("\nCuanto dinero desea retirar-> "))
        saldo -= extra
        print(f"\nDinero en la cuenta al momento: ${saldo}")
    elif opcion == 3:
        print(f"\nSu saldo es-> ${saldo}")
    elif opcion == 4:
        print("\nGracias por usar el cajero automático")
        break
    else:
        print("\nDebe ingresar una opción válida(!)")