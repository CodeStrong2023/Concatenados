
package tienda_libros;

import java.util.Scanner;


public class Tienda_Libros {

    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingrese los siguientes datos del libro:");
        System.out.println("Digite el nombre del libro: ");
        var nombre = entrada.nextLine();
        System.out.println("Digite el ID del libro: ");
        var id = entrada.nextLine();
        System.out.println("Digite el precio del libro: ");
        var precio = entrada.nextLine();
        System.out.println("Indique si el envio es gratuito (Si/No): ");
        var esGratuito = entrada.nextLine();
        
        
        
        System.out.println("Nombre: " + nombre);
        System.out.println("ID: " + id);
        System.out.println("Precio: " + precio);
        System.out.println("Es gratuito?: " + esGratuito);
    }
    
}
