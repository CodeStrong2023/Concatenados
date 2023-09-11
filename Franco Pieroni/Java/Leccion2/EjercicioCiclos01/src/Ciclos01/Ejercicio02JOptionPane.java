/*
  Leer un número e indicar si es positivo o negativo, el proceso se repetira 
  hasta que se introduzca un cero. USAMOS JOPTIONPANE
 */
package Ciclos01;

import javax.swing.JOptionPane;


public class Ejercicio02JOptionPane {
    public static void main(String[] args) {
        int numero = 1;
       
       while (numero != 0){
           numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: ")); 
           if(numero < 0){
               JOptionPane.showMessageDialog(null, "El número ingresado es negativo.");
               
           }
           if (numero > 0){
               JOptionPane.showMessageDialog(null, "El número ingresado es positivo.");
           }
       } 
       JOptionPane.showMessageDialog(null, "Se ingresado cero, el programa ha finalizado."); 
    }
}
