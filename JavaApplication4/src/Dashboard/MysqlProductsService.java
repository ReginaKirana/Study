/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Dashboard;


import static Dashboard.MysqlUtility.getConnection;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 *
 * @author LENOVO
 */
public class MysqlProductsService {
    Connection koneksi = null;

    public MysqlProductsService() {
        koneksi = getConnection(); // asumsi kamu punya DBConnection.java
    }

    public Products makeProdukObject() {
        return new Products();
    }

    public void add(Products produk) throws SQLException {
        String query = "INSERT INTO products (nama, harga, stok) VALUES ('" +
                produk.getNama() + "', " + produk.getHarga() + ", " + produk.getStok() + ", '" +"')";

        try {
            Statement s = koneksi.createStatement();
            s.executeUpdate(query);
            System.out.println("Produk berhasil ditambahkan.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void update(Products produk) throws SQLException {
        String query = "UPDATE produk SET nama = '" + produk.getNama() + 
                       "', harga = " + produk.getHarga() + 
                       ", stok = " + produk.getStok() + 
                       "' WHERE id = " + produk.getId();
        try {
            Statement s = koneksi.createStatement();
            s.executeUpdate(query);
            System.out.println("Produk berhasil diupdate.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void delete(int id) throws SQLException {
        String query = "DELETE FROM produk WHERE id = " + id;
        try {
            Statement s = koneksi.createStatement();
            s.executeUpdate(query);
            System.out.println("Produk berhasil dihapus.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Products getById(int id) throws SQLException {
        Products produk = new Products();
        String query = "SELECT * FROM produk WHERE id = " + id;
        try {
            Statement s = koneksi.createStatement();
            ResultSet rs = s.executeQuery(query);
            if (rs.next()) {
                produk.setId(rs.getInt("id"));
                produk.setNama(rs.getString("nama"));
                produk.setHarga(rs.getInt("harga"));
                produk.setStok(rs.getInt("stok"));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return produk;
    }

    public List<Products> getAll() throws SQLException {
        List<Products> produkList = new ArrayList<>();
        String query = "SELECT * FROM produk";
        try {
            Statement s = koneksi.createStatement();
            ResultSet rs = s.executeQuery(query);
            while (rs.next()) {
                Products produk = new Products();
                produk.setId(rs.getInt("id"));
                produk.setNama(rs.getString("nama"));
                produk.setHarga(rs.getInt("harga"));
                produk.setStok(rs.getInt("stok"));
                produkList.add(produk);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return produkList;
    }

    public void indexReset() throws SQLException {
        String query = "ALTER TABLE produk AUTO_INCREMENT = 1";
        try {
            Statement s = koneksi.createStatement();
            s.executeUpdate(query);
            System.out.println("Auto-increment produk direset.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public boolean isEmpty() {
        String query = "SELECT COUNT(*) FROM produk";
        try {
            Statement s = koneksi.createStatement();
            ResultSet rs = s.executeQuery(query);
            if (rs.next()) {
                return rs.getInt(1) == 0;
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }

    public void closeConnection() {
        if (koneksi != null) {
            try {
                koneksi.close();
                System.out.println("Koneksi ke DB ditutup.");
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
    
    public Products getProductByName(String namaProduk) {
        Products produk = null;
        try {
            String query = "SELECT * FROM products WHERE nama = ?";
            PreparedStatement pst = koneksi.prepareStatement(query);
            pst.setString(1, namaProduk);
            ResultSet rs = pst.executeQuery();
            if (rs.next()) {
                int id = rs.getInt("id");
                int harga = rs.getInt("harga");
                int stok = rs.getInt("stok");

                produk = new Products(id, namaProduk, harga, stok);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return produk;
    }
}