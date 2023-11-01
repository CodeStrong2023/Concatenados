package ingresar;

import javax.swing.JOptionPane;

public class Login extends javax.swing.JFrame {

    public Login() {
        initComponents();
        this.setTitle("Login");
        this.setLocationRelativeTo(null);

    }
    
    private void limpiarCampos() {
        jPasswordUsuario.setText(null);
        jPasswordPass.setText(null);
    }
    
    

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        usuario = new javax.swing.JLabel();
        pass = new javax.swing.JLabel();
        iniciar = new javax.swing.JButton();
        jPasswordPass = new javax.swing.JPasswordField();
        jPasswordUsuario = new javax.swing.JPasswordField();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("Login");
        setPreferredSize(new java.awt.Dimension(300, 200));
        setResizable(false);

        usuario.setText("Usuario:");

        pass.setText("Contraseña:");

        iniciar.setText("Entrar");
        iniciar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                iniciarActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(49, 49, 49)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addComponent(pass)
                            .addComponent(usuario))
                        .addGap(30, 30, 30)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jPasswordPass, javax.swing.GroupLayout.DEFAULT_SIZE, 93, Short.MAX_VALUE)
                            .addComponent(jPasswordUsuario)))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(101, 101, 101)
                        .addComponent(iniciar)))
                .addContainerGap(44, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap(60, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(usuario)
                    .addComponent(jPasswordUsuario, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(pass)
                    .addComponent(jPasswordPass, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(34, 34, 34)
                .addComponent(iniciar)
                .addGap(17, 17, 17))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void iniciarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_iniciarActionPerformed
        if (jPasswordUsuario.getText().equals("") || jPasswordPass.getText().equals("")) {

            JOptionPane.showMessageDialog(null, "Ingrese un usuario y contraseña");
            
        } else {

            if (jPasswordUsuario.getText().equals("admin") && jPasswordPass.getText().equals("admin")) {
                
                this.setVisible(false);
                java.awt.EventQueue.invokeLater(new Runnable() {
                    public void run() {
                        new RegistroPacientes().setVisible(true);
                        
                    }
                });
                
                

            } else {
                JOptionPane.showMessageDialog(null, "Usuario o contraseña incorrectos");
                limpiarCampos();
            }

        }
    }//GEN-LAST:event_iniciarActionPerformed

    

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JButton iniciar;
    private javax.swing.JPasswordField jPasswordPass;
    private javax.swing.JPasswordField jPasswordUsuario;
    private javax.swing.JLabel pass;
    private javax.swing.JLabel usuario;
    // End of variables declaration//GEN-END:variables

    
}
