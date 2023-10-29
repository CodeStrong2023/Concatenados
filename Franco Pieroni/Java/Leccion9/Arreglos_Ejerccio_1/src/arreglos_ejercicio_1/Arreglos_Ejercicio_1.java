/*
Ejercicio 1: Leer 5 números, guardarlos en un arreglo y mostrarlos
en el mismo orden introducidos.
 */
package arreglos_ejercicio_1;

import java.util.Scanner;

public class Arreglos_Ejercicio_1 {

    public static void main(String[] args) {
        Scanner escaner = new Scanner(System.in);
        float[] arreglo = new float[5];

        for (int i = 0; i < 5; i++) {
            System.out.println("Ingrese el " + (i + 1) + "° dígito: ");
            arreglo[i] = escaner.nextFloat();
        }
        
        for (int i = 0; i < 5; i++) {
            System.out.println("El " + i + "° dígito ingresado es: " + arreglo[i]);
        }
    }
}
