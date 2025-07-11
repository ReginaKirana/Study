package com.dicoding.exam.optionalexam2

// TODO
fun minAndMax(number: Int): Int {
    // Mengubah angka menjadi string
    val digits = number.toString().map { it.toString().toInt() }

    // Menemukan digit terkecil dan terbesar
    val minDigit = digits.minOrNull() ?: 0
    val maxDigit = digits.maxOrNull() ?: 0

    // Mengembalikan hasil penjumlahan dari digit terkecil dan terbesar
    return minDigit + maxDigit
}
