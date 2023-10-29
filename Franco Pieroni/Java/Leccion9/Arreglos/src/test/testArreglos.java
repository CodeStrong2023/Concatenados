
package test;


public class testArreglos {
    public static void main(String[] args) {
      //Declaramos variable = instanciamos un objeto del tipo objet
        int edades[] = new int[3];
        System.out.println("edades = " + edades);
        
        edades[0] = 17;
        System.out.println("edades 0 = " + edades[0]);
        
        edades[1] = 18;
        System.out.println("edades 1 = " + edades[1]);
        
        edades[2] = 19;
        System.out.println("edades 2 = " + edades[2]);
        
        // edades[3] = 20; // Dará un erro en tiempo de ejecución, por exeder el tamaño del arreglo
        
        // Recorremos el arreglo
        for (int i = 0; i < edades.length; i++){
            System.out.println("edades y sus elementos " + i + ": " + edades[i]);
        }
        
        
    }
}
