package test;

import domain.Cliente;
import domain.Empleado;
import domain.Persona;
import java.util.Date;

/**
 *
 * @author Gastón
 */
public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Gaston", 57000.0);
        System.out.println("empleado1 = " + empleado1);
        
//        Date fecha1 = new Date();
//        
//        Cliente ciente1 = new Cliente("Bety", 32, 'F', "9 de Julio 1413", fecha1, true);
//        System.out.println("ciente1 = " + ciente1);
//        
//        Persona persona1 = new Persona();
    }
}
