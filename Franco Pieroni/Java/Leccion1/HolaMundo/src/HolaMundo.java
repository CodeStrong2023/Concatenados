 import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
        System.out.println("Hola Perri!");
        
        String miVariable = "Soy una variable :)";
        System.out.println(miVariable);
        miVariable = "Como estas? :)";
        System.out.println(miVariable);
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Como te llamas?");
        String nombre = scanner.nextLine();
        
        System.out.println("Hola " + nombre + "!");
        
    }
} 
 