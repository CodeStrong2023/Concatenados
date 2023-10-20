var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+apellido;
console.log(nombreCompleto);

var nombreCompleto2 = 'Gastón'+' '+'Marenco';
console.log(nombreCompleto2);

var juntos = nombre + 219; // Lee de izq a der siguiendo la cadena lee el numero como srt
console.log(juntos);
juntos = nombre + (78 + 17); // Aquí se puede diferenciar a través de los parentesis
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; // Tercera Concatenación usando el operador simplificado
console.log(nombre);

// Hoy ya no se una var, se utiliza let y const
let nombre2 = 'Pedro';
console.log(nombre2);

const apellido2 = 'Lepes';
// apellido2 = 'Peres'; una constante no puede ser modificada
console.log(apellido2);

let x, y; // Se pueden crear varias variables dentro de una misma línea
x = 17, y = 21; // Se puede hacer asignación de varias variables dentro de la misma línea
let z = x + y; // Se asigna el valor de la operación
console.log(z);

let _1num = 31; // No utilizar números para iniciar el nombre de una variable
let rompiendo = 'rompe'; // No utilizar palabras reservadas para variables

console.log(_1num);
console.log(rompiendo);

// Almpliando el uso de var, let y const
/*
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que se sobreescriba
*/

var nombre = 'Gastón';
nombre = 'Lionel';
console.log(nombre);

function saludar(){
    var nombre3 = 'Cristiano';
    console.log(nombre3);
}
//console.log(nombre3); // Aquí no lee el dato en la función

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); // En la función funciono correctamente, en la estructura if fallo

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque
solo disponible dentro de un bloque de llaves
o dentro de una función
*/

function saludar2(){
    let nombre2= 'Gastón';
    console.log(nombre2);
}
//console.log(nombre2)

if(true){
    let edad2 = 33;
    console.log(edad2);
}
//console.log(edad2);

/*
const se utiliza para valores constantes que no pueden ser reasignados
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); // solo se ejecuta el console anterior