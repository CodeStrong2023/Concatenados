// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriaos que es identica
*/

// Tipo Str
var nombre = 'Gastón';
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);

// Tipo Númerico
var numero = 3000;
console.log(numero);

// Tipo Objeto
var objeto = {
    nombre: "Gastón",
    apellido: "Marenco",
    edad: 20
};
console.log(objeto);

// Tipo de dato boolean
var bandera = true;
console.log(typeof bandera);

// Tipo de dato función
function miFuncion(){}
console.log(typeof miFuncion);

// Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

// Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona)

// Tipo de dato undefined
var x;
console.log(x);

x = undefined
console.log(typeof x);

// null: significa ausencia de valor
var y = null; // null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

// Tipo de dato array y Empty String
var autos = ['Citroen','Audi','BMW','Ford'];
console.log(autos);
console.log(typeof autos); // Preguntamos que tipo de dato es:

var z = '';
console.log(z); // Esto se refiere a que es una cadena vacía:
console.log(typeof z);