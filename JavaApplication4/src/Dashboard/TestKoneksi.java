package Dashboard;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author LENOVO
 */
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class TestKoneksi {
    public static void main(String[] args) {
        // Sesuaikan host, port, nama db
        String url = "jdbc:mysql://localhost:3307/sirielshop";
                // sesuaikan username dan password
        String user = "root";
        String password = "Sungchan8@1";

        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            if (conn != null) {
                System.out.println("Koneksi ke MySQL BERHASIL!");
                conn.close(); // jangan lupa ditutup
            }
        } catch (SQLException e) {
            System.out.println("Koneksi GAGAL!");
            e.printStackTrace();
        }
    }
}
