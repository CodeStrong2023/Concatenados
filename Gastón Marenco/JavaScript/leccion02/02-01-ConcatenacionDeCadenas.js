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