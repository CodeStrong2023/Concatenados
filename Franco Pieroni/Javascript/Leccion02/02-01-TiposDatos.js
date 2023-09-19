var nombre = 'Ariel';
console.log(typeof nombre); //Tipo string
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
var numero = 3000;
console.log(numero); //Tipo numerico

var objeto = {
    nombre : 'Ariel',
    apellido : 'Betancud',
    telefono : '261456879',
    clase : 'Programación' 
}

console.log(objeto);

//Tipo de dato boolean
var bandera = true
console.log(bandera);

//Tipo de dato función
function miFuncion(){}
console.log(typeof miFuncion)

//Tipo de dato symbol
var simbolo = Symbol('Mi simbolo');
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
    contructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);

// Tipo de variable undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

// null: significa ausencia de  valor
var y = null; //null no es un tipo de dato, pero su origen es de tipo object
console.log(typeof y);

// Tipo de dato Array y Empty String
var autos = ['Citroen','Audi','BMW','Ford'];
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z); // Esto se refiere a que es una cadena vacia
console.log(typeof z);