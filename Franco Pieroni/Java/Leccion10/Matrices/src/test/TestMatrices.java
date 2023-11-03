
package test;

import domain.Persona;


public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int[3][2];
        System.out.println("edades = " + edades);
        edades[0][0] = 5;
        edades[0][1] = 7;
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 20;
        edades[2][1] = 23;
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 2; j++) {
                System.out.println("edades " + "[" + i + "]" + "[" + j + "]: " + edades[i][j]);
            }
        }
        
        
        // String frutas[][]  = new String[3][2]; Sintaxis clásica
        
        // Sintaxis Simplificada:
        
        String frutas[][] = {{"Limon", "Pomelo"},{"Ciruela", "Kiwi"},{"Banana", "Manzana"}};
               
//        for (int i = 0; i < frutas.length; i++) {
//            for (int j = 0; j < frutas[i].length; j++) {
//                System.out.println("frutas " + "[" + i + "]" + "[" + j + "]: " + frutas[i][j]);
//            }
//        }
        imprimir(frutas);
        // Creamos una matriz de objetos
        Persona personas[][] = new Persona[2][3];
        // Asignamos valores a la matriz
        personas[0][0] = new Persona("Franco");
        personas[0][1] = new Persona("Guido");
        personas[0][2] = new Persona("Fer");
        personas[1][0] = new Persona("Mati");
        personas[1][1] = new Persona("Lucho");
        personas[1][2] = new Persona("Santi");
        imprimir(personas);
                          
    }
    
    public static void imprimir(Object matriz[][]){
        
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                
                System.out.println("matriz " + "[" + i + "]" + "[" + j + "]: " + matriz[i][j]);
                
            }
        }      
        
    }
}
