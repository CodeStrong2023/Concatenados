package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

/**
 *
 * @author Gastón
 */
public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        
        Orden orden1 = new Orden();
        //Agregamos productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        //Tarea:
        //Crear mas objetos de tipo Producto = 10
        //Crear mas objetos de tipo Orden = 2
        
        Producto producto3 = new Producto("Remera", 4500.00);
        Producto producto4 = new Producto("Gorra", 5000.00);
        Producto producto5 = new Producto("Bufanda", 2000.00);
        Producto producto6 = new Producto("Zapatillas", 14000.00);
        Producto producto7 = new Producto("Medias", 1500.00);
        Producto producto8 = new Producto("buzo", 22000.00);
        Producto producto9 = new Producto("Camisa", 9000.00);
        Producto producto10 = new Producto("Guantes", 3000.00);
        Producto producto11 = new Producto("Chaqueta", 5200.00);
        Producto producto12 = new Producto("Chanclas", 2999.00);
        
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.agregarProducto(producto12);
        orden2.agregarProducto(producto10);
        orden2.mostrarOrden();
        
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto6);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto11);
        orden3.agregarProducto(producto9);
        orden3.mostrarOrden();
    }
}
