package ejercicio5;

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Digite la primer calificacion: ");
        float nota1 = Float.parseFloat(entrada.nextLine());
        System.out.print("Digite la segunda calificacion: ");
        float nota2 = Float.parseFloat(entrada.nextLine());
        System.out.print("Digite la tercer calificacion: ");
        float nota3 = Float.parseFloat(entrada.nextLine());
        float suma = nota1 + nota2 + nota3;

        System.out.println("Suma: " + suma);
    }

}
