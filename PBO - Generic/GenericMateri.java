// ===============================================
// Materi: Pengenalan dan Penerapan Generic di Java
// ===============================================
import java.util.*;
// ============================
// 1. Pengertian Generic
// ============================
// Generic adalah fitur di Java yang memungkinkan kita membuat kelas, interface, atau method
// yang bisa bekerja dengan berbagai tipe data, tanpa harus mendefinisikan ulang untuk setiap tipe.
// Tujuan utama: type-safety, reusable, dan fleksibel.

public class GenericMateri {
    // ====================================
    // 2. Contoh Kelas Generic: Box<T>
    // ====================================
    // Kelas ini bisa menyimpan data dari tipe apapun.
    static class Box<T> {
        private T isi;

        public void setIsi(T isi) {
            this.isi = isi;
        }

        public T getIsi() {
            return isi;
        }
    }

    // ==========================================
    // 3. Contoh Generic Method (Metode Generik)
    // ==========================================
    // Metode ini bisa menerima data bertipe apapun.
    public static <T> void cetakIsi(T data) {
        System.out.println("Isi data: " + data);
    }
    // ============================================================
    // 4. Contoh Generic dengan Bounded Type (Batasan Tipe)
    // ============================================================
    // T hanya boleh merupakan subclass dari Number
    public static <T extends Number> double kuadrat(T angka) {
        return angka.doubleValue() * angka.doubleValue();
    }

    public static void main(String[] args) {
        // =============================
        // 5. Penggunaan Kelas Generic
        // =============================
        Box<String> kotakString = new Box<>();
        kotakString.setIsi("Halo Generics");
        System.out.println("Kotak berisi: " + kotakString.getIsi());

        Box<Integer> kotakInteger = new Box<>();
        kotakInteger.setIsi(42);
        System.out.println("Kotak berisi: " + kotakInteger.getIsi());

        // ================================
        // 6. Pemakaian Metode Generic
        // ================================
        cetakIsi("Contoh generic method");
        cetakIsi(12345);
        cetakIsi(3.14);

        // =============================================
        // 7. Pemakaian Bounded Type (T extends Number)
        // =============================================
        System.out.println("Kuadrat dari 4: " + kuadrat(4));
        System.out.println("Kuadrat dari 2.5: " + kuadrat(2.5));

        // ==========================================
        // 8. Generic di Collection Framework (Java)
        // ==========================================
        List<String> daftarNama = new ArrayList<>();
        daftarNama.add("Siti");
        daftarNama.add("Budi");

        for (String nama : daftarNama) {
            System.out.println("Nama: " + nama);
        }

        // Tanpa Generic (TIDAK DISARANKAN karena tidak type-safe)
        // List daftarCampur = new ArrayList();
        // daftarCampur.add("Teks");
        // daftarCampur.add(123);
        // Bisa error saat dijalankan jika tidak hati-hati casting-nya

        
    }
}

// ===============================================
// Kesimpulan:
// - Generic membuat kode lebih aman dan fleksibel
// - Menghindari casting dan runtime error
// - Sangat penting dalam struktur data modern seperti List, Map, Stack, dll
// ===============================================