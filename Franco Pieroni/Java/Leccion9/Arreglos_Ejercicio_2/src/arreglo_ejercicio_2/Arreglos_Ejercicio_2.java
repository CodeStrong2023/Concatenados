/*
Ejercicio 2: Leer 5 números, guardarlos en un arreglo y mostrarlos en el orden inverso al 
introducido.
*/

package arreglo_ejercicio_2;

import java.util.Scanner;


public class Arreglos_Ejercicio_2 {
    

    public static void main(String[] args) {
        Scanner escaner = new Scanner(System.in);
        float[] arreglo = new float[5];

        for (int i = 0; i < 5; i++) {
            System.out.println("Ingrese el " + (i + 1) + "° dígito: ");
            arreglo[i] = escaner.nextFloat();
        }
        
        for (int i = 4; i >= 0; i--) {
            System.out.println("El " + i + "° dígito ingresado es: " + arreglo[i]);
        }
    }
}
