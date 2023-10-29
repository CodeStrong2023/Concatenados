
/*
Ejercicio 3: Leer 5 números por teclado, almacenarlos en 
un arreglo y a continuación realizar la media de los números positivos,
la media de los negativos y contar el número de ceros.
*/

package arreglos_ejercicio_3;

import java.util.Scanner;


public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner escaner = new Scanner(System.in);
        float arreglo[] = new float[5];
        int cantidadPositivos = 0;
        int totalPositivos = 0;
        int cantidadNegativos = 0;
        int totalNegativos = 0;
        float mediaPositivos = 0;
        float mediaNegativos = 0;
        int ceros = 0;

        for (int i = 0; i < 5; i++) {
            System.out.println("Ingrese el " + (i + 1) + "° dígito: ");
            arreglo[i] = escaner.nextFloat();
            
            if (arreglo[i] > 0){
                cantidadPositivos++;
                totalPositivos += arreglo[i];
            } 
            
            if (arreglo[i] < 0){
                cantidadNegativos++;
                totalNegativos += arreglo[i];
            }
             
            if (arreglo[i] == 0) {
                ceros++;
            }
        }
        
        mediaPositivos = totalPositivos / cantidadPositivos;
        mediaNegativos = totalNegativos / cantidadNegativos;
        
        System.out.println("Media de Positivos: " + mediaPositivos);
        System.out.println("Media de Negativos: " + mediaNegativos);
        System.out.println("Cantidad de ceros: " + ceros);
        
    }
}
