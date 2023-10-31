package Ciclos06;

import javax.swing.JOptionPane;

/**
 *
 * @author Gastón
 */
public class Ejercicio06 {
    public static void main(String[] args) {
        int numero, suma = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma += numero;
        }while(numero != 0);
        JOptionPane.showMessageDialog(null, "\nLa suma de todos los numeros ingresados es: "+suma);
    }
}
