// Ejercicio 1: Calcular estación del año
let mes = 7;
let estacion;  //Undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor corresponde a la estación de: "+estacion)

//Ejercicio 2: Hora del día
let horaDia = 20;
let mensaje;
if(horaDia >= 6 && horaDia <=11){
    mensaje = "Good morning"
}
else if(horaDia >= 12 && horaDia <=16){
    mensaje = "Good afternoom"
}
else if(horaDia >= 17 && horaDia <=19){
    mensaje = "Good evening"
}
else if(horaDia >= 20 && horaDia <=23){
    mensaje = "Good night"
}
else{
    mensaje = "Valor incorrecto"
}
console.log(mensaje)

//Estructura switch(la sintaxis es igual a Java)
switch(mes){  //No solo se pueden utilizar números, también cadenas
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenido a la estación de: "+estacion)

//Evitar repetir tu código
//Dry don`t repeat yourself

let days = 'Sabado';
switch (days) {
    case 'Lunes':
        console.log('Hoy es '+days)
        break;

    case 'Martes':
        console.log('Hoy es '+days)
        break;
    
    case 'Miercoles':
        console.log('Hoy es '+days)
        break;

    case 'Jueves':
        console.log('Hoy es '+days)
        break;

    case 'Viernes':
        console.log('Hoy es '+days)
        break;

    case 'Sabado':
        console.log('Hoy es '+days)
        break;

    case 'Domingo':
        console.log('Hoy es '+days)
        break;

    default:
        console.log('Error en el ingreso del dia de la semana')
        break;
}

//Esta es la opción mejorada

let days2 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
function getDay(n){
    if(n <1 || n > 7){
        throw new Error('out of range');
    }
    return days2[n-1];
}
console.log(getDay(5));

//Hacer un Ejercicio similar al que esta hecho, pero ahora con los
//meces del año, debes hacerlo con la estructura switch y luego con
//la función en la opcion mejorada

let month = 'Febrero';
switch (month) {
    case 'Enero':
        console.log('Hoy es '+month)
        break;

    case 'Febrero':
        console.log('Hoy es '+month)
        break;
    
    case 'Marzo':
        console.log('Hoy es '+month)
        break;

    case 'Abril':
        console.log('Hoy es '+month)
        break;

    case 'Mayo':
        console.log('Hoy es '+month)
        break;

    case 'Junio':
        console.log('Hoy es '+month)
        break;

    case 'Julio':
        console.log('Hoy es '+month)
        break;

    case 'Agosto':
        console.log('Hoy es '+month)
        break;

    case 'Septiembre':
        console.log('Hoy es '+month)
        break;

    case 'Octubre':
        console.log('Hoy es '+month)
        break;

    case 'Noviembre':
        console.log('Hoy es '+month)
        break;

    case 'Diciembre':
        console.log('Hoy es '+month)
        break;
        

    default:
        console.log('Error en el ingreso del mes del año')
        break;
}

//Esta es la opción mejorada

let month2 = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
function getMonth(n){
    if(n <1 || n > 12){
        throw new Error('out of range');
    }
    return month2[n-1];
}
console.log(getMonth(2));