/*
Ejercicio 8: Pedir un número N, y mostar todos los números
del 1 al N
*/
package Ciclos08;

import java.util.Scanner;

/**
 *
 * @author Gastón
 */
public class Ciclos08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(entrada.nextLine());
        int i = 1;
        while(i <= numero){
            System.out.println(i);
            i++;
        }
    }
}
