# Ejercicio 4: Calculadora de impuestos
# Crear una función para calcular el total del pago incluyendo
# un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuestos: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxxx

# Creamos la función que calcula el total del pago incluyendo el impuesto
def calculadora_impuestos(pago_sin_impuesto,impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecutamos la función
pago_sin_impuesto = float(input('Digite el pago sin impuestos: '))
impuesto = float(input('Digite el monto del impuesto a aplicar: '))
pago_con_impuesto = calculadora_impuestos(pago_sin_impuesto, impuesto)
print(f'El pago con impuestos es: {pago_con_impuesto}')