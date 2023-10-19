
package domain;


public class Empleado extends Persona{ 
    @Override
    public void imprimir() {
        System.out.println("Método para impirmir desde la clase hija");
    }
}
