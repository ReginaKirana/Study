# ----------------------------------------------------------------------
# Nama File    : Bressenham.py
# Deskripsi    : Berisi implemetasi algoritma Bressenham dalam pembuatan Garis
# Tanggal      : 1 Maret 2025
# ----------------------------------------------------------------------

import time
import matplotlib.pyplot as plt

def bressenham(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    p = 2 * dy - dx
    y = y0

    koordinat = []

    for x in range (x0, x1+1):
        koordinat.append((x, y))
        # print(f" x = {x}, y = {y}, p = {p}") #Debugging

        if p < 0:
            p += 2 * dy
        else:
            y += 1
            p += 2 * (dy - dx)

    return koordinat
    
# Inisialisasi titik awal dan akhir
x0, y0 = 0, 0
x1, y1 = 10000, 10000

# Hitung titik titik garis
start_time = time.perf_counter()
garis_bressenham = bressenham(x0, y0, x1, y1)

# Hitung runtime Bressenham
end_time = time.perf_counter()

# cetak runtime
runtime = end_time - start_time
print(f"Runtime Bressenham: {runtime:.8f} detik")

# Gambar hasil
x_val, y_val = zip(*garis_bressenham)
plt.plot(x_val, y_val, 'ro-')
plt.grid()
plt.show()