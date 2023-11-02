// Ejercicio 1: Calcular estación del año


let mes = 4;
let estacion;
if (mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano;"
}
else if (mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño;"
}
else if (mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno;"
}
else if (mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera;"
}
else{
    estacion = "Valor incorrecto"
}

console.log("El valor corresponde a la estación de: " +estacion);

// Ejercicio 2: Hora del día

let horaDia = 9;
let mensaje;

if (horaDia >= 6 && horaDia <= 11){
    mensaje = "Buen día!;"
}
else if (horaDia >= 12 && horaDia <= 16){
    mensaje = "Good afternoom;"
}
else if (horaDia >= 17 && horaDia <= 19){
    mensaje = "Buenas tardes!;"
}
else if (horaDia >= 20 && horaDia <= 23){
    mensaje = "Buenas noches!;"
}
else{
    mensaje = "Valor incorrecto"
}

console.log(mensaje)

// Estructura switch(la sintaxis es igual a Java)

switch(mes){ // No solo se pueden utilizar números, tambien cadenas
    case 1: case 2: case 12:
    estacion = "Verano"
    break;
    case 3: case 4: case 5:
    estacion = "Otoño"
    break;
    case 6: case 7: case 8:
    estacion = "Invierno"
    break;
    case 9: case 10: case 11:
    estacion = "Primavera"
    break;
    default:
        estacion = "Valor incorrecto";
}

console.log("Bienvenido a la estación de: " +estacion);