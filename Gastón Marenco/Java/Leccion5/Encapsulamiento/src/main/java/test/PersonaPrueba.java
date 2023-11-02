package test;

import dominio.Persona;

/**
 *
 * @author Gastón
 */
public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio";  //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre);  //Error
        System.out.println("persona1 con su nombre modificado: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        //Tarea: Crear otro objeto de tipo Persona, asignar valores de manera inicial
        //y imprimir, luego modificar sus valores y volver a imprimir
        Persona persona2 = new Persona("Pepe", 500, false);
        
        System.out.println("Nombre: "+persona2.getNombre());
        System.out.println("Sueldo en dolares: "+persona2.getSueldo());
        System.out.println("Esta eliminado: "+persona2.isEliminado());
        
        //Modificando valores
        persona2.setNombre("Antonio");
        persona2.setSueldo(900);
        persona2.setEliminado(true);
        
        System.out.println("Nombre: "+persona2.getNombre());
        System.out.println("Sueldo en dolares: "+persona2.getSueldo());
        System.out.println("Esta eliminado: "+persona2.isEliminado());
        
        System.out.println("persona1: "+persona1.toString());
        System.out.println("persona1 = " + persona1);
    }
}
