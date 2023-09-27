/*
 
 */
package Clases;


public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona();//LLamamos al constructor
        persona1.nombre = "Ariel";//El hexadecimal normalmente empiezan con 0x
        persona1.apellido= "Betacund";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Ovaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion();
    }
}
