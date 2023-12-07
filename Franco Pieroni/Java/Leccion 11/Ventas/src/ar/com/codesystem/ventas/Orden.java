
package ar.com.codesystem.ventas;

public class Orden {
    // Atributos de la clase
    private int idOrden;
    private Producto productos[]; // Declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;
    
    // Constructor vacio 
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }
    
    // Método para agregar un producto al arreglo
    public void agregarProducto(Producto producto){
        if(this.contadorProductos < Orden.MAX_PRODUCTOS){
            this.productos[this.contadorProductos++] = producto;
        }
        else{
            System.out.println("Se ha superado el máximo de productos: " + Orden.MAX_PRODUCTOS);
        }
    }
    
    // Método para calcular el total de precio de productos
    public double calcularTotal(){
        double total = 0; // Variable temporal
        for (int i = 0; i < this.contadorProductos; i++) {
            //Producto producto = this.productos[i];   
            // total += producto.getPrecio();
            total += this.productos[i].getPrecio(); // Lo de arriba en una sola linea
        }
        return total;
    }
    
    // Método para impirmir el detalle de todos los productos y del total de la Orden
    public void mostrarOrden(){
        System.out.println("Id Orden: " + idOrden);
        double totalOrden = this.calcularTotal();
        System.out.println("El total de la Orden es : $" + totalOrden);
        System.out.println("Productos de la orden: ");
        for (int i = 0; i < this.contadorProductos; i++) {
            System.out.println(this.productos[i]);
        }
    }
}
