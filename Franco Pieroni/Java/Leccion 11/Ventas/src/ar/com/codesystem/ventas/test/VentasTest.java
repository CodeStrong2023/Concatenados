
package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {
    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        Producto producto3 = new Producto("Buzo", 20000.00);
        Producto producto4 = new Producto("Gorra", 14400.00);
        Producto producto5 = new Producto("Bermuda", 16600.00);
        Producto producto6 = new Producto("Bufanda", 8000.00);
        Producto producto7 = new Producto("Camisa", 21100.00);
        Producto producto8 = new Producto("Remera", 19900.00);
        Producto producto9 = new Producto("Medias", 5500.00);
        Producto producto10 = new Producto("Bolso", 39900.00);
        Producto producto11 = new Producto("Mochila", 55500.00);
        Producto producto12 = new Producto("Pullover", 29900.00);
        
        Orden orden1 = new Orden();
        // Agregamos productos
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        Orden orden2 = new Orden();
        // Agregamos productos
        orden1.agregarProducto(producto3);
        orden1.agregarProducto(producto5);
        orden1.agregarProducto(producto7);
        orden1.agregarProducto(producto9);
        orden1.agregarProducto(producto11);
        orden1.mostrarOrden();
        
        Orden orden3 = new Orden();
        
        orden1.agregarProducto(producto4);
        orden1.agregarProducto(producto6);
        orden1.agregarProducto(producto8);
        orden1.agregarProducto(producto10);
        orden1.agregarProducto(producto12);
        orden1.mostrarOrden();
        
        // Tarea:
        // Crear mas objetos del tipo producto = 10
        // Crear mas objetos del tipo Orden = 2
    }
}
