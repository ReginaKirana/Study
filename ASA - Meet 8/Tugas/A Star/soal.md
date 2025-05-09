## A* Pathfinding in a Grid Maze
Diberikan sebuah grid 2D berukuran N x M, di mana setiap sel dapat berupa jalan kosong (0) atau rintangan (1). Anda harus mencari jalur terpendek dari titik awal (sx, sy) ke titik tujuan (gx, gy) menggunakan algoritma A*. Jika tidak ada jalur, kembalikan -1.

Grid dapat dilalui secara horizontal dan vertikal (tidak diagonal), dan setiap langkah memiliki biaya tetap = 1. Fungsi heuristik yang digunakan adalah Manhattan Distance.

### Input Format
Baris pertama: dua bilangan bulat N dan M (jumlah baris dan kolom)
Baris kedua: empat bilangan bulat sx sy gx gy (koordinat awal dan tujuan)
Berikutnya N baris masing-masing berisi M elemen 0 atau 1 (grid)

### Constraints
1 <= N, M <= 100
0 <= sx, sy, gx, gy < max(N, M)
Koordinat (sx, sy) dan (gx, gy) selalu berada di dalam grid dan bukan rintangan
Sel 1 adalah rintangan, tidak dapat dilalui
Hanya pergerakan atas, bawah, kiri, kanan yang diperbolehkan

### Output Format
Satu bilangan bulat: panjang jalur terpendek dari start ke goal, atau -1 jika tidak ada jalur.

### Sample Input 0
3 3
0 0 2 2
0 0 0
0 1 0
0 0 0

### Sample Output 0
4

### Sample Input 1
1 1
0 0 0 0
0

### Sample Output 1
0

### Sample Input 2
5 5
0 0 4 4
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 0 0 0 0

### Sample Output 2
8