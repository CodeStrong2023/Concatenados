
package hospital;
import java.util.Scanner;
import javax.swing.JOptionPane;




public class Hospital {
    
    public static int i,opcion_1;
    public static int idPaciente = 0;
    public static String datosPaciente[][] = new String[idPaciente][7];
    public static boolean switch_1 = false;
    
    public static void LimpiarPantalla() {
        System.out.print("\033[H\033[2J");  
        System.out.flush();  
    }
    public static void Menu(){
        
        Scanner entrada = new Scanner(System.in);
        
        while (switch_1 == false) {
            System.out.println("");
            System.out.println("                              ****************    ");
            System.out.println("                              SISTEMA HOSPITAL    ");
            System.out.println("                              ****************    ");
            System.out.println("");
            System.out.println("                           1) Ingresar paciente");
            System.out.println("                           2) Buscar paciente");
            System.out.println("                           3) Modificar paciente");
            System.out.println("                           4) Eliminar paciente");
            System.out.println("                           5) Salir");
            System.out.println("");
            System.out.println("                           Elija una opción:> \n");
            opcion_1 = Integer.parseInt(entrada.nextLine());
            
            
            
            if (opcion_1 == 5){
                switch_1 = true;
            }
            else {
                if (opcion_1 == 4) {
                    
                }
                else{
                    if (opcion_1 == 3) {
                        
                    }
                    else {
                        if (opcion_1 == 2) {
                    
                        }
                        else {
                            if (opcion_1 == 1) {
                    
                            }
                            else {
                                
                                System.out.println("");
                                System.out.println("");
                                System.out.println("                              ****************    ");
                                System.out.println("                              SISTEMA HOSPITAL    ");
                                System.out.println("                              ****************    ");
                                System.out.println("");
                                System.out.println("                      Debe ingresar una opción válida(!)");
                                System.out.println("                    Digite cualquier tecla para continuar: >  ");
                            }
                        }
                    }
                }
            } 
        }
    }
    
    public static void main(String[] args) {
        Menu();
    }
    
    
}


   
    