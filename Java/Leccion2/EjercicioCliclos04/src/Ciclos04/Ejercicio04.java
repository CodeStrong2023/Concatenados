/*
Ejercicio 4:Pedir números hasta que se teclee uno negativo,
y mostrar cúantos números se han introducido.
Lo hacemos primero con la clase Scanner
Y luego lo hacemos con la clase JOptionPane
 */
package Ciclos04;

import javax.swing.JOptionPane;


public class Ejercicio04 {
    public static void main(String[] args) {
        int numero, conteo = 0;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        while(numero >= 0){
            JOptionPane.showMessageDialog(null, "El número "+numero+" es POSITIVO");
            conteo++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));
        }
        JOptionPane.showMessageDialog(null, "A ingresado "+conteo+" números que no son negativos");
    
    }
}
