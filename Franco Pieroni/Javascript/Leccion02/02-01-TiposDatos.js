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