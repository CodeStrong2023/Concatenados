/*
Ejercicio 2: con la clase JOptionPane
Leer un número e indicar si es positivoo
negativo. El proceso se repetira hasta que se introduzca 
un cero 0
 */
package Ciclos02;

import javax.swing.JOptionPane;

public class Ciclos02 {
    public static void main(String[] args) {
        
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero != 0){
            if (numero > 0){
                JOptionPane.showMessageDialog(null, "El número "+numero+" es POSITIVO");
            }
            else{
                JOptionPane.showMessageDialog(null, "El número "+numero+" es NEGATIVO");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showConfirmDialog(null, "El número "+numero+" finaliza el programa");
    }
}
 
