/*
 Ejercicio 1: Leer un número y mostrar su cuadrado, repetir el proceso 
 hasta que se introduzca un número negativo.
*/
package Ciclos01;

import javax.swing.JOptionPane;

/*
Usamos la classe JoptionPane para resolver el ejercicio
*/
public class Ejercicio01 {
    public static void main(String[] args) {
        
        int numero = 0;
        
        while(numero >= 0){
            
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: ")); 
            System.out.println("El cuadrado de " + numero + " es igual a: " + numero * numero);
        }
        
        System.out.println("Se ha ingresado un número negativo");
        
    }
}
