package ejercicio7;

import java.util.Scanner;

public class Ejercicio7 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingrese el nombre del vendedor: ");
        var nombre = entrada.nextLine();
        
        System.out.print("Ingrese la cantidad de autos vendidos: ");
        int autosVendidos = Integer.parseInt(entrada.nextLine());
        
        final float salarioBasico = 1000;
        float comision = autosVendidos * 150;
        float comisionValorTotal = 0;
        double valorTotal = 0;
        
        System.out.println("Ingrese los valores de venta de los " + (autosVendidos) + " autos: ");
        
        for (int i = 0;autosVendidos > i;i++)
        {
            System.out.print("" + (i + 1) + ": ");
            float valorAuto = Float.parseFloat(entrada.nextLine());
            double comisionAuto = valorAuto * 0.05;
            valorTotal = valorTotal + comisionAuto;
        }
        
        double salarioTotal = salarioBasico + comision + valorTotal;
        System.out.println("El salario total del vendedor " + nombre + " sera de: " + salarioTotal + "$ este mes.");
        
        
        
        

        
    }

}
