
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1; 
        persona1 = new Persona(); // Llamamos al Constructor (Intanciamos, es decir creamos un objeto)
        persona1.nombre = "Franco"; // Damos valores al objeto persona1
        persona1.apellido = "Pieroni";  // Se guarda el atributo en un bloque de memoria cuya dirección se nos mostrara en valor hexadecimal 0x 
        persona1.obtenerInformacion(); // Usamos el metodo creado anteriormente para ver los atributos
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Guido";
        persona2.apellido = "Pieroni";
        persona2.obtenerInformacion();
        
    }
 
}
