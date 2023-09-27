
package caja; // package


public class Caja { //Clase pública caja
    // Atributos (características)
    int ancho;
    int alto;
    int profundo;
    // Métodos y constructores
    public Caja() {  // Constructor1  = VACIO  
        
    }
    // Constructor con parámetros
    public Caja(int ancho, int alto, int profundo){
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen() {
        return ancho * alto * profundo;
    }

    
}
