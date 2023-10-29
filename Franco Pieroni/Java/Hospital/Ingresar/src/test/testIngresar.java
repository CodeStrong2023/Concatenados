package test;

import ingresar.Paciente;
import ingresar.RegistroPacientes;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class testIngresar {

    public static void main(String[] args) {

        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new RegistroPacientes().setVisible(true);
            }
        });
        
    }
}
