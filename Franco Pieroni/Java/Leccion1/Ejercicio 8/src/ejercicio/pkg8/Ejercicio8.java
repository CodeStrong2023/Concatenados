
package ejercicio.pkg8;

public class Ejercicio8 {
    
    public static void main(String[] args) {
        var num = 4;
        var numTexto = "Numero desconocido";
        
        if(num == 1){
            numTexto = "Numero Uno";
        }
        else if (num == 2){
            numTexto = "Numero Dos";
        }
        else if (num == 3){
            numTexto = "Numero Tres";
        }
        else if (num == 4){
            numTexto = "Numero Cuatro";
        }
        else{
            numTexto = "Numero Desconocido";
        }
        
        System.out.println("numTexto = " + numTexto);
    }
    
}
