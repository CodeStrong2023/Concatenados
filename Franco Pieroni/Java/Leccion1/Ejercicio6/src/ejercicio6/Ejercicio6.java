
package ejercicio6;

import java.util.Scanner;


public class Ejercicio6 {

    
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        System.out.print("Digite cuanto dinero tiene Guillermo: ");
        float dineroGuille = Float.parseFloat(entrada.nextLine());
        float dineroLuis = dineroGuille / 2;
        float dineroJuan = (dineroGuille + dineroLuis) / 2;

        float total = dineroGuille + dineroLuis + dineroJuan;

        System.out.println("Entre Guillermo, Luis y Juan tienen: " + total + "$");
    }
    
}
