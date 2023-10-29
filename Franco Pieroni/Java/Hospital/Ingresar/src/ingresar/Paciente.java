package ingresar;

public class Paciente extends Persona {
    

    private int idPaciente;
    static int contadorPaciente;
    private String tipoSangre;
    private String especialidad;
    
    Paciente() {

    }

    public Paciente(int idPaciente, String tipoSangre, String especialidad, String nombre, String apellido, String dni, String fechaNacimiento) {

        super(nombre, apellido, dni, fechaNacimiento);
        Paciente.contadorPaciente++;
        this.idPaciente = Paciente.contadorPaciente;
        this.tipoSangre = tipoSangre;
        this.especialidad = especialidad;

    }

    public static int getContadorPaciente() {
        return contadorPaciente;
    }

    public static void setContadorPaciente(int aContadorPaciente) {
        contadorPaciente = aContadorPaciente;
    }
    
    public int getIdPaciente() {
        return this.idPaciente;
    }

    public void setIdPaciente(int idPaciente) {
        this.idPaciente = idPaciente;
    }

    public String getTipoSangre() {
        return this.tipoSangre;
    }

    public void setTipoSangre(String tipoSangre) {
        this.tipoSangre = tipoSangre;
    }

    public String getEspecialidad() {
        return this.especialidad;
    }

    public void setEspecialidad(String especialidad) {
        this.especialidad = especialidad;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Paciente{");
        sb.append("idPaciente=").append(idPaciente);
        sb.append(", tipoSangre=").append(tipoSangre);
        sb.append(", especialidad=").append(especialidad);
        sb.append('}');
        return sb.toString();
    }

    

    
}
