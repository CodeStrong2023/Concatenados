package ingresar;

// Importamos las librerías necesarias para crear el formulario y un arreglo de pacientes 
import static java.lang.Integer.parseInt;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import javax.swing.JOptionPane;
import javax.swing.table.DefaultTableModel;

public class RegistroPacientes extends javax.swing.JFrame {

    // Creamos una nueva tabla llamada (modelo)
    DefaultTableModel modelo = new DefaultTableModel();
    
    // Creamos un arreglo de pacientes
    ArrayList<Paciente> listaPacientes = new ArrayList<Paciente>();
    
    public int contadorPacientes = 0;

    // Aquí se formateara el formulario y la tabla
    public RegistroPacientes() {
        initComponents();
        this.setTitle("REGISTRO PACIENTES");
        this.setSize(800, 600);
        this.setLocationRelativeTo(null);
        modelo.addColumn("ID");
        modelo.addColumn("NOMBRE");
        modelo.addColumn("APELLIDO");
        modelo.addColumn("DNI");
        modelo.addColumn("FECHA DE NACIMIENTO");
        modelo.addColumn("TIPO SANGUÍNEO");
        modelo.addColumn("ESPECIALIDAD");
        // Usamos esté método para que la tabla se actualice
        refrescarTabla();

    }
    // Este método permite actualizar la tabla
    public void refrescarTabla() {

        // Elimina todos los elementos de la tabla
        while (modelo.getRowCount() > 0) {
            modelo.removeRow(0);
        }
        // Por cada paciente en el arreglo (listaPacientes) se creará un objeto de 7 elementos
        for (Paciente paciente : listaPacientes) {
            Object p[] = new Object[7];
            // En cada elemento se almacenarán los diferentes datos de la tabla
            p[0] = paciente.getIdPaciente();
            p[1] = paciente.getNombre();
            p[2] = paciente.getApellido();
            p[3] = paciente.getDni();
            p[4] = paciente.getFechaNacimiento();
            p[5] = paciente.getTipoSangre();
            p[6] = paciente.getEspecialidad();
            // Se agrega la fila a la tabla
            modelo.addRow(p);
        }
        // Se agrega el modelo a la tabla (datosPacientes)
        datosPacientes.setModel(modelo);

    }
   
    
    
    // Este método nos permite verificar que el nombre y apellido ingresados sean válidos
    public boolean validarNombre(){
        // Usamos expresiones regulares para esto
        // Si los String ingresados (nombre) o (apellido) tienen algún caracter que no sea una letra
        if (!nombre.getText().matches("[A-Za-z]*") || !apellido.getText().matches("[A-Za-z]*")){
            // retorna false
            return false;
        } else {
            // Sino retorna true
            return true;
        }
    }

    // Esté método nos permite validar que el DNI ingresado sea válido
    public boolean validarDni() {
        int valido = 0;
        String numero = "";
        String[] unoNueve = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
        boolean validLength = true;
        boolean esNumero = false;

        // Se comprobará que el DNI ingresado tengo un largo válido
        if (dni.getText().length() > 8 || dni.getText().length() < 7) {

            validLength = false;

        }

        // Y que el String esté compuesto  solo de dígitos
        int length = dni.getText().length();

        for (int i = 0; i < dni.getText().length(); i++) {
            numero = dni.getText().substring(i, i + 1);

            for (int j = 0; j < unoNueve.length; j++) {
                if (numero.equals(unoNueve[j])) {
                    valido++;
                }
            }
        }

        if (valido == dni.getText().length()) {

            esNumero = true;

        }

        // Si se cumplen ambas condiciones retorna (true)
        if (validLength == true && esNumero == true) {
            return true;
        } else {
            return false;
        }

    }
    // Este método verifica que la fecha ingresada por el usuario sea válida
    public boolean validarFecha() {
        // Para ello se utilizan expresiones regulares
        String fecha = fechaNacimiento.getText();
        // Se estabelce un patrón usando la clase Pattern
        Pattern pattern = Pattern.compile("^(?:3[01]|[12][0-9]|0?[1-9])([\\-/.])(0?[1-9]|1[1-2])\\1\\d{4}$");
        // Con la clase Matcher comprobamos si la fecha ingresada encajacon el patrón 
        Matcher matcher = pattern.matcher(fecha);
        // Si encaja, retorna true
        if (matcher.matches()) {
            return true;
        } else {
            return false;
        }

    }
    // Este método permite verificar que no hayan pacientes repetidos en la lista de pacientes 
    public boolean validarPaciente() {
        int coincidencias = 0;
        // Itera por el ArrayList de Pacientes listaPacientes
        for (Paciente paciente : listaPacientes){
            // Si el dni ingresado es igual al de algun paciente ya registrado
            if (dni.getText().equals(paciente.getDni().toString())){
                coincidencias++;
            }
        }
        // Se retorna true
        if (coincidencias > 0){
            return true;
        } else {
            return false;
        }
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jScrollPane2 = new javax.swing.JScrollPane();
        jTextArea1 = new javax.swing.JTextArea();
        jScrollPane1 = new javax.swing.JScrollPane();
        datosPacientes = new javax.swing.JTable();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        tipoSangre = new javax.swing.JComboBox<>();
        especialidad = new javax.swing.JComboBox<>();
        fechaNacimiento = new javax.swing.JFormattedTextField();
        btnEliminarAlumno = new javax.swing.JButton();
        btnAgregarAlumo = new javax.swing.JButton();
        nombre = new javax.swing.JTextField();
        apellido = new javax.swing.JTextField();
        dni = new javax.swing.JTextField();
        btBuscar = new javax.swing.JButton();
        btModificar = new javax.swing.JButton();

        jTextArea1.setColumns(20);
        jTextArea1.setRows(5);
        jScrollPane2.setViewportView(jTextArea1);

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        datosPacientes.setModel(new javax.swing.table.DefaultTableModel(
            new Object [][] {
                {null, null, null, null, null, null, null},
                {null, null, null, null, null, null, null},
                {null, null, null, null, null, null, null},
                {null, null, null, null, null, null, null}
            },
            new String [] {
                "id", "Nombre", "Apellido", "DNI", "Fecha de nacimiento", "Tipo sanguineo", "Especialidad"
            }
        ));
        jScrollPane1.setViewportView(datosPacientes);

        getContentPane().add(jScrollPane1, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 350, 820, 170));

        jLabel1.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        jLabel1.setText("Nombre:");
        getContentPane().add(jLabel1, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 40, -1, -1));

        jLabel2.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        jLabel2.setText("Apellido:");
        getContentPane().add(jLabel2, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 90, -1, -1));

        jLabel3.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        jLabel3.setText("Fecha de nacimiento:");
        getContentPane().add(jLabel3, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 180, 150, 30));

        jLabel4.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        jLabel4.setText("DNI:");
        getContentPane().add(jLabel4, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 140, -1, -1));

        jLabel5.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        jLabel5.setText("Tipo de sangre:");
        getContentPane().add(jLabel5, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 230, -1, -1));

        jLabel6.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        jLabel6.setText("Especialidad requerida:");
        getContentPane().add(jLabel6, new org.netbeans.lib.awtextra.AbsoluteConstraints(10, 280, -1, -1));

        tipoSangre.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "A+", "B+", "AB+", "0+", "A-", "B-", "AB-", "0-" }));
        getContentPane().add(tipoSangre, new org.netbeans.lib.awtextra.AbsoluteConstraints(180, 230, -1, -1));

        especialidad.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Cardiología", "Odontología", "Traumatología", "Pediatria", "Clínica", "Radiología", "Dermatología", "Oftalmología" }));
        getContentPane().add(especialidad, new org.netbeans.lib.awtextra.AbsoluteConstraints(180, 280, -1, -1));

        fechaNacimiento.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                fechaNacimientoActionPerformed(evt);
            }
        });
        getContentPane().add(fechaNacimiento, new org.netbeans.lib.awtextra.AbsoluteConstraints(180, 180, 150, -1));

        btnEliminarAlumno.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        btnEliminarAlumno.setText("Eliminar");
        btnEliminarAlumno.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnEliminarAlumnoActionPerformed(evt);
            }
        });
        getContentPane().add(btnEliminarAlumno, new org.netbeans.lib.awtextra.AbsoluteConstraints(560, 190, 170, 100));

        btnAgregarAlumo.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        btnAgregarAlumo.setText("Agregar");
        btnAgregarAlumo.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnAgregarAlumoActionPerformed(evt);
            }
        });
        getContentPane().add(btnAgregarAlumo, new org.netbeans.lib.awtextra.AbsoluteConstraints(560, 50, 170, 100));

        nombre.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                nombreActionPerformed(evt);
            }
        });
        getContentPane().add(nombre, new org.netbeans.lib.awtextra.AbsoluteConstraints(80, 40, 250, -1));
        getContentPane().add(apellido, new org.netbeans.lib.awtextra.AbsoluteConstraints(80, 90, 250, -1));
        getContentPane().add(dni, new org.netbeans.lib.awtextra.AbsoluteConstraints(80, 140, 250, -1));

        btBuscar.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        btBuscar.setText("Buscar");
        getContentPane().add(btBuscar, new org.netbeans.lib.awtextra.AbsoluteConstraints(380, 50, 170, 100));

        btModificar.setFont(new java.awt.Font("Segoe UI", 1, 14)); // NOI18N
        btModificar.setText("Modificar");
        getContentPane().add(btModificar, new org.netbeans.lib.awtextra.AbsoluteConstraints(380, 190, 170, 100));

        pack();
    }// </editor-fold>//GEN-END:initComponents
    // Aquí estableceremos que pasará la usar el botón "Eliminar"
    private void btnEliminarAlumnoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnEliminarAlumnoActionPerformed
        
      
      
        
        
    }//GEN-LAST:event_btnEliminarAlumnoActionPerformed
    // Aquí estableceremos que pasará la usar el botón "Agregar"
    private void btnAgregarAlumoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnAgregarAlumoActionPerformed

        // Primero nos aseguramos de que el usuario no deje ningun campo sin completar
        if (nombre.getText().equals("") || apellido.getText().equals("") || dni.getText().equals("") || fechaNacimiento.getText().equals("")) {
            // De lo contrario se le notifica que debe llenar todos los campos
            JOptionPane.showMessageDialog(null, "Debe llenar todos los campos");
        // Luego se validara el nombre y apellido ingresado   
        } else if (!validarNombre()){
            // Si no son válidos se solicita que los vuelva a ingresar
            JOptionPane.showMessageDialog(null, "Debe ingresar un nombre y apellido válidos");
        // Luego se compruba que el DNI ingresado sea válido 
        } else if (!validarDni()) {
            // Si es inválido se notifica al usuario
            JOptionPane.showMessageDialog(null, "Debe ingresar un DNI válido");
        // Se valida la fecha ingresada     
        } else if (!validarFecha()) {
            // Si no es válida se solicita volver a ingresar en el formato correcto
            JOptionPane.showMessageDialog(null, "Debe ingresar una fecha válida, en el formato dd-mm-aaaa");
        // Por último se verifica que el paciente no  se encuentra ya creado en listaPacientes 
        } else if (validarPaciente()) {
            
            JOptionPane.showMessageDialog(null, "El paciente ingresado ya existe");
            
        } else {
            
            // Se crea el nuevo paciente y se almacenan los datos ingresados en los atributos
            Paciente paciente = new Paciente();
            paciente.setIdPaciente(Paciente.contadorPaciente++);
            paciente.setNombre(nombre.getText());
            paciente.setApellido(apellido.getText());
            paciente.setDni(dni.getText());
            paciente.setFechaNacimiento(fechaNacimiento.getText());
            paciente.setTipoSangre(tipoSangre.getSelectedItem().toString());
            paciente.setEspecialidad(especialidad.getSelectedItem().toString());
            // Se agrega el nuevo paciente a la lista 
            listaPacientes.add(paciente);
            // Se actualiza la tabla
            refrescarTabla();

        }


    }//GEN-LAST:event_btnAgregarAlumoActionPerformed

    private void nombreActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_nombreActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_nombreActionPerformed

    private void fechaNacimientoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_fechaNacimientoActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_fechaNacimientoActionPerformed

    // Se declaran las variables del formulario
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JTextField apellido;
    private javax.swing.JButton btBuscar;
    private javax.swing.JButton btModificar;
    private javax.swing.JButton btnAgregarAlumo;
    private javax.swing.JButton btnEliminarAlumno;
    private javax.swing.JTable datosPacientes;
    private javax.swing.JTextField dni;
    private javax.swing.JComboBox<String> especialidad;
    private javax.swing.JFormattedTextField fechaNacimiento;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JTextArea jTextArea1;
    private javax.swing.JTextField nombre;
    private javax.swing.JComboBox<String> tipoSangre;
    // End of variables declaration//GEN-END:variables

    private void assertTrue(boolean find) {
        throw new UnsupportedOperationException("Not supported yet."); 
    }
}
