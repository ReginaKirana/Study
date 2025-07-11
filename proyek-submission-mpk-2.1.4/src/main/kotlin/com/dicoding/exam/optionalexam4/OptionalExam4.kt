package com.dicoding.exam.optionalexam4

// TODO
fun getMiddleCharacters(string: String): String {
    val length = string.length
    val middle = length / 2

    return if (length % 2 == 0) {
        // Jika panjang string genap, kembalikan 2 karakter tengah
        string.substring(middle - 1, middle + 1)
    } else {
        // Jika panjang string ganjil, kembalikan 1 karakter tengah
        string[middle].toString()
    }
}