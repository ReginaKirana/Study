package YT;


public class GenericsExample {
    public static void main(String[] args) {
        // Tanpa kelas Generik
        IntegerPrinter printer = new IntegerPrinter(23);
        printer.print();
        // Kalo mau print double atau tipe data lain ga bisa

        // Dengan Kelas Generik
        Printer <Integer> printer2 = new Printer(25);
        printer2.print();

        Printer <Double> DoublePrinter = new Printer(99.87);
        System.out.println("== Double ==");
        DoublePrinter.print();

        // Tipe kelas sama namun tipe data beda, tanpa casting

    }
}
