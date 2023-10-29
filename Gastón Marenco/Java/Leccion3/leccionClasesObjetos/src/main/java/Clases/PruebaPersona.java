package Clases;

/**
 *
 * @author Gastón
 */
public class PruebaPersona {

    public static void main(String[] args) {
        Persona persona1 = new Persona();  //Llamamos al constructor

        persona1.nombre = "Gaston";  //El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Marenco";

        persona1.obtenerInformacion();

        Persona persona2 = new Persona();

        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);

        persona2.obtenerInformacion();
        
        persona2.nombre = "Lionel";
        persona2.apellido = "Messi";
        
        persona2.obtenerInformacion();
    }
}
