// Ejercicio para encontrar números pares

let parInpar = 2;
if(parInpar % 2 == 0){
    console.log("Es un número par")
} else {
    console.log("Es un número inpar")
}

// Ejercicio es mayor de edad

let edad = 2;
if(edad > 18){
    console.log("Es mayor de edad")
} else {
    console.log("Es menor de edad")
}


// Ejercicio dentro de un rango
let dentroRango = 0; // Aquí vamos a ir cambiando el valor
let valMin = 0, valMax = 10;
if (dentroRango >= valMin && dentroRango <= valMax){
    console.log("Está dentro del rango")
} else {
    console.log("Esta fuera del rango")
}

// Ejercicio: si el padre puede asistir al juego de su hijo
let vacaciones = false, diaDescanso = false;
if (vacaciones || diaDescanso){
    console.log("El padre puede asistir al juego de su hijo")
}else {
    console.log("El padre no puede asistir al juego de su hijo")
}

// Operador ternario
let resultado2 = 3 > 3 ? "Verdadero" : "Falso" 
console.log(resultado2)
let numero = 9;
resultado2 = numero % 2 == 0 ? "Es un número PAR" : "Es un número IMPAR";
console.log(resultado2)

// Convertir String a Number
let miNumero = "10"; // Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero) // Esta es una función
console.log(typeof edad2)
if(isNaN(edad2)){  // Not a Number, no es un número
    console.log("Esta variable no contiene solo números")
}else {
    if(edad2 >= 18){
        console.log("Puede votar");
    }else {
        console.log("Muy joven para votar");
    }
}


let resultado3 = edad >= 18 ? "Puede votar " : "Muy joven para votar";
console.log(resultado3);