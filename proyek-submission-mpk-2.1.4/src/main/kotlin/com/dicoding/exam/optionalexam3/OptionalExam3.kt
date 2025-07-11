package com.dicoding.exam.optionalexam3

// TODO
fun manipulateString(str: String, int: Int): String {
    // Mencari angka dalam string menggunakan Regex
    val regex = "\\d+".toRegex() // Menemukan angka dalam string
    val matchResult = regex.find(str)

    return if (matchResult != null) {
        // Jika ada angka dalam string, ekstrak angka dan kalikan dengan input integer
        val numberInString = matchResult.value.toInt()
        val result = numberInString * int

        // Gabungkan teks tanpa angka dengan hasil perkalian
        str.replace(matchResult.value, "") + result
    } else {
        // Jika tidak ada angka, gabungkan string dengan input integer
        str + int
    }
}
