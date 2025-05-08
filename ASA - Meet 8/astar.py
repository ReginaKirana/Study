import heapq
import math

# Fungsi untuk menghitung jarak Euclidean (heuristik) antara dua titik (lintang, bujur)
def euclidean_distance(p1, p2):
    lat1, lon1 = p1
    lat2, lon2 = p2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

# Fungsi A* untuk mencari jalur terpendek
def a_star(start, goal, graph):
    open_set = [(0 + euclidean_distance(city_coords[start], city_coords[goal]), 0, start)]  # (f_score, g_score, node)
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        _, current_g, current = heapq.heappop(open_set)  # Ambil node dengan f_score terkecil
        
        if current == goal:
            # Jika kita sudah sampai goal, kembalikan jalur yang ditempuh
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Balikkan jalur agar dari start ke goal
        
        # Mengeksplorasi tetangga dari node current
        for neighbor, weight in graph[current]:
            tentative_g = current_g + weight  # Menggunakan berat (biaya perjalanan antar kota)
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + euclidean_distance(city_coords[neighbor], city_coords[goal])
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
    
    return None  # Tidak ada jalur ditemukan

# Koordinat (latitude, longitude) untuk beberapa kota
city_coords = {
    'A': (1.0, 1.0),
    'B': (1.0, 2.0),
    'C': (2.0, 2.0),
    'D': (3.0, 2.0),
    'E': (2.0, 1.0),
}

# Graph berbentuk dictionary yang menunjukkan kota dan tetangganya dengan biaya perjalanan (dalam km)
graph = {
    'A': [('B', 1), ('E', 1.5)],
    'B': [('A', 1), ('C', 1.5)],
    'C': [('B', 1.5), ('D', 2)],
    'D': [('C', 2)],
    'E': [('A', 1.5), ('C', 1)],
}

# Koordinat start dan goal
start = 'A'
goal = 'D'

# Menjalankan A* untuk mencari jalur terpendek dari A ke D
path = a_star(start, goal, graph)
print(f"Jalur terpendek dari {start} ke {goal}:", path)

# Output jarak total
if path:
    total_distance = 0
    for i in range(len(path) - 1):
        current = path[i]
        next_node = path[i + 1]
        for neighbor, weight in graph[current]:
            if neighbor == next_node:
                total_distance += weight
                break
    print(f"Total jarak: {total_distance} km")