/*
 Ejercicio 1: Leer un número y mostrar su cuadrado, repetir el proceso 
 hasta que se introduzca un número negativo.
*/

package Ciclos01;

/*
 Usamos la clase Scanner para resolver el ejercicio
*/
import java.util.Scanner;


public class Ciclos01 {
    public static void main(String[] args) {
        
        int numero;
        
        Scanner scanner = new Scanner(System.in);
        numero =  0;
        
        while(numero >= 0){
            System.out.println("Ingrese un número, si ingresa un número negativo el programa terminará: ");
            numero =  Integer.parseInt(scanner.nextLine());
            System.out.println("El cuadrado de " + numero + " es: " + numero * numero);
        }
        
        System.out.println("Se ha ingresado un número negativo");
    }
}
