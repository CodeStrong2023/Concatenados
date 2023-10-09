
package test;

import dominio.Persona; 

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Franco", 57000,false);
        System.out.println("persona1 su nombre es: " + persona1.getNombre());
        // Modificamos a través de métodos
        persona1.setNombre("Guido");
        System.out.println("persona1 con su nombre modificado: " + persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: " + persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: " + persona1.isEliminado());
        
        // Tarea: crear otro objeto del tipo Persona, asignar valores de manera inicial 
        // y imprimir, luego modificar sus valores y volver a imprimir
        
        Persona persona2 = new Persona("Fernando", 120000, false);
        System.out.println("persona2 su nombre es: " + persona2.getNombre());
        System.out.println("persona2 su sueldo es: " + persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: " + persona2.isEliminado());
        
        persona2.setNombre("Matias");
        persona2.setSueldo(500000);
        persona2.setEliminado(true);
        
        System.out.println("persona2 su nombre modificado es: " + persona2.getNombre());
        System.out.println("persona2 su sueldo modificado es: " + persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano modificado: " + persona2.isEliminado());
       
        System.out.println("persona1: " + persona1.toString());
        System.out.println("persona2: " + persona2.toString());
    }
}
