def is_safe(board, row, col):
    # Cek kolom di atas
    for i in range(row):
        if board[i] == col:
            return False
        
        # Cek diagonal kiri atas dan kanan atas
        if abs(board[i] - col) == abs(i - row):
            return False
            
    return True

def backtrack(row):
    if row == n:
        # Konversi solusi dalam bentuk papan
        solution = []
        for i in range(n):
            line = ['.'] * n
            line[board[i]] = 'Q'
            solution.append(''.join(line))
        hasil.append(solution)
        return
    
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Tempatkan ratu
            backtrack(row + 1)
            board[row] = -1  # Backtrack

# Inisialisasi variabel
n = 4  # Ukuran papan (8x8)
board = [-1] * n  # Menyimpan posisi ratu (board[row] = col)
hasil = []  # Menyimpan semua solusi

# Mulai algoritma backtracking
backtrack(0)

# Cetak jumlah solusi
print(f"Jumlah solusi untuk papan {n}x{n}: {len(hasil)}")

# Cetak semua solusi
if hasil:
    for i, solution in enumerate(hasil):
        print(f"\nSolusi {i+1}:")
        for row in solution:
            print(row)