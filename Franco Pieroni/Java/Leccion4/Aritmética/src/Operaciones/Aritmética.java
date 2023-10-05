
package Operaciones;


public class Aritmética { // La Clase siempre usa Pacal case, es decir comienza con mayúscula
    // Atributos de Clase
    int a; // Por default se asigna 0 a las variables;
    int b;
    
    // El constructor es un método especial
    
    public Aritmética(){ // Constructor 1 vacio
        System.out.println("Se está ejecutando el constructor número 1");
    }
    
    
    public Aritmética(int a, int b){ // Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se está ejecutndo el constructor número 2");
    }
    
    // Métodos, definimos un método sumarNumeros
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("La suma de los dígitos es: " + resultado);
    }
    
    public int sumarConRetorno() {
        int resultado = a + b;
        return resultado;
    }
    
    public int sumarConArgumentos(int a, int b) {
        this.a = a; // El argumento a se asigna al atributo this.a
        this.b = b; 
        //return a + b;
        return this.sumarConRetorno();
    }
}
 