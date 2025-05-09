def tucoTaco(n):
    jmlKombinasi = 0 # jumlah kombinasi awal 0

    def backtrack(topping_awal, topping_pasangan):
        nonlocal jmlKombinasi
        # Jika jumlah topping lengkap dan valid
        if topping_awal == n and topping_pasangan == n:
            jmlKombinasi += 1
            return
        # Tambah topping awal jika masih kurang dari n
        if topping_awal < n:
            backtrack(topping_awal + 1, topping_pasangan)
        # Tambah topping pasangan hanya jika tidak melebihi topping awal
        if topping_pasangan < topping_awal:
            backtrack(topping_awal, topping_pasangan + 1)

    backtrack(0, 0)
    return jmlKombinasi

# Input
n = int(input())  
print(tucoTaco(n))