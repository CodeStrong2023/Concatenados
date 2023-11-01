package ingresar;

public class Usuario {

    private String usuario;
    private String pass;

    public Usuario(String usuario, String pass) {
        this.usuario = usuario;
        this.pass = pass;
    }

    private void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    private void setPass(String pass) {
        this.pass = pass;
    }

    private String getUsuario() {
        return usuario;
    }

    private String getPass() {
        return pass;
    }
    
    Usuario admin = new Usuario("admin", "admin");
}
