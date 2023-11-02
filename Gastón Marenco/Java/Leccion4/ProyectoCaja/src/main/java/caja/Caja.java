/*
Proyecto caja:
Ejercicio 1: Crear un proyecto según las especificaciones
mostradas a continuación.
La formula es: volumen = ancho * alto * profundidad
*/
package caja;

/**
 *
 * @author Gastón
 */
public class Caja {  //Clase publica caja
    //Atributos(Caracteristicas)
    int ancho;
    int alto;
    int profundo;
    //Metodos y constructores(acciones)
    
    public Caja(){  //Constructor 1 = vacio
    }
    //Constructor con parametros
    public Caja(int ancho, int alto, int profundo){  //Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    }
    
    public int calcularVolumen(){  //Metodo para calcular
        return ancho * alto * profundo;
    }
}
