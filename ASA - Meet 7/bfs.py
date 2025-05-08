# =========================================
# Nama File    : Breadth First Search
# Deskripsi    : Program untuk menerapkan algoritma Breadth First Search (BFS) pada Graf
# Nama         : Regina Sasikirana Farikh 
# NIM          : 24060123140155
# Tanggal      : 10 Maret 2025
# =========================================

# =========================================
#       Breadth-First Search (BFS)
# =========================================
# 📌 Apa itu BFS?
# Breadth-First Search (BFS) adalah algoritma pencarian atau traversal dalam graf atau pohon.
# BFS menjelajahi semua node pada level yang sama sebelum beralih ke level berikutnya.

# 📌 Kelebihan & Kekurangan BFS:
# Kelebihan:
# 1. Menemukan jalur terpendek dalam graf tak berbobot.
# 2. Cocok untuk eksplorasi graf skala kecil hingga menengah.
# Kekurangan:
# Butuh lebih banyak memori dibanding DFS untuk menyimpan node di antrian.

# =========================================
#           CODE BFS (Python)
# =========================================
from collections import deque

def bfs(graph, start_vertex):
    # Error Handling
    if start_vertex not in graph:
        print(f"Error: Node '{start_vertex}' tidak ditemukan dalam graf.")
        return []
    
    visited = set()                 # Menyimpan node yang sudah dikunjungi
    queue = deque([start_vertex])   # Queue untuk BFS (FIFO)
    visited.add(start_vertex) 

    print("BFS Traversal:", end=" ")
    while queue:
        vertex = queue.popleft()    # Ambil node dari depan antrian
        print(vertex, end=" ")      # Cetak node yang dikunjungi

        for neighbor in graph[vertex]:      # Periksa semua tetangga
            if neighbor not in visited:
                visited.add(neighbor)       # Tandai sebagai dikunjungi
                queue.append(neighbor)      # Masukkan ke queue
    print()


# Contoh Aplikasi
# Graph1 (Alfabet)
graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
# BFS dari node 'A'
bfs(graph1, 'A')
bfs(graph1, 'K')

# Graph2 (Angka)
graph2 = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6'],
    '4': ['2'],
    '5': ['2', '6'],
    '6': ['3', '5', '7'],
    '7': ['6']
}
# BFS dari node '1'
bfs(graph2, '1')
bfs(graph2, '99')