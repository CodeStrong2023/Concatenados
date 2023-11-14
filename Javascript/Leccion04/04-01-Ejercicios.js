//Ejercicio 1: Calcular estacion del año
let mes = "9";
let estacion; //Undefiend
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
console.log("El valor corresponde a la estación de: "+estacion);

//Ejercicio 2: Hora del día
/*
de 6 a 11 nos saluda: Good Morning
de 12 a 16 nos saluda: Good afternoom
de 17 a 19 nos saluda: Good evening
de 20 a 23 nos saluda: Good night
Trabajaremos con 24 horas
*/
let horaDia = 7;
let mensaje;
if(horaDia >= 6 && horaDia <= 11){
    mensaje = "Goos morning";
}
else if(horaDia >= 12 && horaDia <= 16){
    mensaje = "Goos afternoom";
}
else if(horaDia >= 17 && horaDia <= 19){
    mensaje = "Goos evening";
}
else if(horaDia >= 20 && horaDia <= 23){
    mensaje = "Goos night";
}
else{
    mensaje = "Valor incorrecto";
}
console.log(mensaje);

//Estructura switch(la sintaxis es igual a Java)
switch(mes){//No solo se pueden utilizar número, también cadenas
    case 1: case 2: case 12: 
    estacion = "Verano";
    break;
case 3: case 4: case 5:    
    estacion = "Otoño";
    break
case 6: case 7: case 8:
    estacion = "Invierno";
    break;
case 9: case 10: case 11:
    estacion = "Primavera";
    break;
default:
    estacion = "Valor incorrecto";        

}
console.log("Bienvenido a la estación de: "+estacion);

//ampliando el uso del var let y const
/*
Con var puedes reasignar en cualquier momento
este forma parte del ambito global 
Un error es que se sobreescriba
*/

var nombre = 'Ariel';
nombre = 'Osvaldo';
console.log(nombre);

function saludar(){
    var nombre3 = 'Natalia';
    console.log(nombre3);
}
//console.log(nombre3); //Aquí no lee el dato en la función 


if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la función funciono correctamente, en la estructura if fallo

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una función
*/

function saludar2(){
    let nombre2 = 'Ariel';
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

/*
const se utiliza para valores constantes que no pueden ser reasignadoas
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta el console anterior

//Evitar repetir tu código
//Dry don´t  repeat yourself
//let days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
let days = 1;
switch (days) {
    case 1:
        console.log('hoy es Lunes')
        break;
    case 2:
        console.log('hoy es Martes')
    case 3:
        console.log('hoy es Miercoles')
    case 4:
         console.log('hoy es Jueves')
    case 5:
        console.log('hoy es Viernes')
    case 6:
        console.log('hoy es Sabado')
    case 7:
        console.log('hoy es Domingo')
    default:
        console.log("Error en el ingreso del día de la semana");
        break;
}

//Esta es la opcion mejorada 


let days2 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'];
function getDay(n){
    if(n < 1 || n > 7){
        throw new Error('out of range');
    }
    return days [n-1];
}

console.log(getDay(7));
 
//Hacer un ejercicio similiar al que esta hecho, pero ahora con los
//meses del año, debes hacerlo con la estructura switch y luego con
//la función en la opción mejorada

let month = 11;
switch (days) {
    case 1:
        console.log('Es Enero')
        break;
    case 2:
        console.log('Es Febrero')
    case 3:
        console.log('Es Marzo')
    case 4:
         console.log('Es Abril')
    case 5:
        console.log('Es Mayo')
    case 6:
        console.log('Es Junio')
    case 7:
        console.log('Es Julio')
    case 8:
         console.log('Es Agosto')
    case 9:
        console.log('Es Septiembre')
    case 10:
        console.log('Es Octubre')
    case 11:
        console.log('Es Noviembre')
    case 12:
        console.log('Es Diciembre')
    default:
        console.log("Error en el ingreso del mes del año");
        break;
}

//Esta es la opcion mejorada 

let month2 = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
function getDay(n){
    if(n < 1 || n > 12){
        throw new Error('out of range');
    }
    return days [n-1];
}

console.log(getDay(1));