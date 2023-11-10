
public class Hospital {
    public static void main(String[] args) {
      
        System.out.println("Manuel: "+validarNombre("Manuel"));
        System.out.println("Fernando: "+validarNombre("Fernando"));
        System.out.println("Jose: "+validarNombre("Jose"));
        System.out.println("Martina: "+validarNombre("Martina"));
        System.out.println("Matias: "+validarNombre("Matias"));
        
    }
    public static boolean validarNombre(String nombre){
        
        return nombre.matches("^([A-Z]{1}[a-z]+[ ]?){1,2}$");
    }
}
