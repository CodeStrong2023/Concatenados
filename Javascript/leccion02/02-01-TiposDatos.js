// Tipos de Datos en JavaScript 
/*
La sintaxis en lo que es comentarios
es muy similar en la de Java 
realmente diriamos que es identica
*/
// Tipo String
var nombre = 'Ariel'; // Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
//Tipo Numerico 
var numero = 3000; 

console.log(numero);

var objeto = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "2614567893"

}

console.log(objeto);

// Tipo de dato Boolean
var bandera = true;
console.log(typeof bandera);

// Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion); 

// Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo)

// Tipo de dato clase
class Persona{
    contructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona)

//Tipo de dato undefined
var x;
console.log(x);

x = undefined;
console.log(typeof x);

// null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

//Tipo de dato array y Emppty String
var autos = ['Citroen','Audi','BMW','Ford']
console.log(autos);
console.log(typeof autos); //Preguntamos que tipo de dato es:

var z = '';
console.log(z); //Esto se refiere a que es una cadena vacia:
console.log(typeof z);