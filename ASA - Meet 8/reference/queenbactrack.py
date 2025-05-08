def is_safe(board, row, col):
    for i in range(row):
        # Cek kolom
        if board[i] == col:
            return False
        # Cek diagonal
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

# Bagian testing
if __name__ == "__main__":
    n = 4  # Ubah sesuai kebutuhan
    board = [-1] * n
    hasil = []

    backtrack(0)

    print(f"Jumlah solusi untuk {n}-Queen: {len(hasil)}\n")
    for idx, sol in enumerate(hasil):
        print(f"Solusi {idx + 1}:")
        for line in sol:
            print(line)
        print()