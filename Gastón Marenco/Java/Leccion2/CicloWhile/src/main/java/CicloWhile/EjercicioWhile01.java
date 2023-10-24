package CicloWhile;

/**
 *
 * @author Gastón
 */
public class EjercicioWhile01 {

    public static void main(String[] args) {
        
        System.out.println("\nCiclo While:");
        var conteo = 0;  // Inferencia de tipos
        while (conteo < 3) {
            System.out.println("conteo = " + conteo);
            conteo++;  // Vamos aumentando en 1 la variable
        }
        
        System.out.println("\nCiclo Do While:");
        var contador = 0;
        do{
            System.out.println("contador = " + contador);
            contador++;
        }while(contador < 7);
        
        System.out.println("\nCiclo For:");
        for(var contando = 0; contando < 7; contando++){
            System.out.println("contando = " + contando);
        }
    }
}
