
package Operaciones;


public class PruebaAritmetica {
    public static void main(String[] args) {
        
        var a = 10; // Variales locales
        int b = 7;  // Memoria Stack
        miMetodo(); // Llamamos al método nuevo
        Aritmética aritmetica1 = new Aritmética();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        
        // Para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado );
        
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos: " + resultado);
        
        System.out.println("Aritmetica1 a: " + aritmetica1.a );
        System.out.println("Aritmetica1 b: " + aritmetica1.b );
        
        Aritmética aritmetica2 = new Aritmética(5, 8);
        System.out.println("aritmetica2 = " + aritmetica2.a);
        System.out.println("aritmetica2 = " + aritmetica2.b);
        
        // aritmetica1 = null; nunca utilizar esto, no se debe hacer
        // System.gc(); método para limpiar residuos, es pesado, no utilizar
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona = " + persona);
        System.out.println("persona nombre = " + persona.nombre);
        System.out.println("persona nombre = " + persona.apellido);
    }
    // Modularidad creamos un nuevo método
    public static void miMetodo(){
        // a = 10; // una variable está limitada
        System.out.println("Aquí hay otro método");
    }
}

class Persona{ // Clase tipo default o package
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){ // Constructor
        super(); // Llamada al constructor de la clase Padre -> object
        // Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this); 
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: " + this);
    }
}

class Imprimir{
    public Imprimir(){
        super(); // El constructor de la clase padre, para reservar memoria
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: " + persona);
        System.out.println("Impresión del objeto actual");
    }
}
