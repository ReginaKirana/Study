# ----------------------------------------------------------------------
# Nama File    : DDA.py
# Deskripsi    : Berisi implemetasi algoritma DDA dalam pembuatan Garis
# Tanggal      : 1 Maret 2025
# ----------------------------------------------------------------------

import time
import matplotlib.pyplot as plt

def dda (x0, y0, x1, y1):
    # (x0, y0) = titik awal
    # (x1, y1) = titik akhir
    dx = x1 - x0
    dy = y1 - y0
    
    # step
    if (abs(dy) > abs(dx)):
        step = abs(dy)
    else:
        step = abs(dx)

    if step == 0:
        return [(x0,y0)]
        
    x_inc = dx/step
    y_inc = dy/step

    x, y = x0, y0
    points = []

    for i in range (step + 1):
        points.append((round (x), round(y)))
        # print(f"Step {i}: ({round(x)}, {round(y)})")
        x += x_inc
        y += y_inc
    
    return points

# Testing
# Inisialisasi titik awal dan akhir
x0, y0 = 0,0
x1, y1 = 10000, 10000

# Hitung titik titik garis
start_time = time.perf_counter()
garis = dda(x0, y0, x1, y1)
end_time = time.perf_counter()

# cetak runtime
runtime = end_time - start_time
print(f"Runtime DDA: {runtime:.8f} detik")

# Gambar hasil
x_val, y_val = zip(*garis)
plt.plot(x_val, y_val, 'bo')
plt.grid()
plt.show()