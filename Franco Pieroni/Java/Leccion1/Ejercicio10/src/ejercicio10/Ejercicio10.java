
package ejercicio10;


public class Ejercicio10 {

    
    public static void main(String[] args) {
        var num = 4;
        var numTexto = "Numero desconocido";
        
        switch(num){
            case 1:
                numTexto = "Numero Uno";
                break;
            case 2:
                numTexto = "Numero Dos";
                break;
            case 3:
                numTexto = "Numero Tres";
                break;
            case 4:
                numTexto = "Numero Cuatro";
                break;
            default: 
                numTexto = "Caso no encontrado";
        }
        
        System.out.println("NumTexto = " + numTexto);
    }
    
}
