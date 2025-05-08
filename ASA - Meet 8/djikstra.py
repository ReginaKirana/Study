import heapq

def dijkstra(graph, start):
    # graph: dict {node: [(neighbor, weight), ...]}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh graf berbobot
    # Format: {node: [(tetangga, bobot), ...]}
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    
    # Menjalankan algoritma Dijkstra dari node start 'A'
    start_node = 'A'
    result = dijkstra(graph, start_node)
    
    # Menampilkan hasil
    print(f"Jarak terpendek dari node {start_node}:")
    for node, distance in result.items():
        print(f"Ke {node}: {distance}")
    
    # Contoh tambahan: mencari jalur terpendek dengan pelacakan predecessor
    def dijkstra_with_path(graph, start):
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        predecessors = {node: None for node in graph}
        queue = [(0, start)]
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))
        
        return distances, predecessors
    
    # Fungsi untuk merekonstruksi jalur dari node awal ke tujuan
    def reconstruct_path(predecessors, start, end):
        path = []
        current = end
        
        while current != start:
            path.append(current)
            current = predecessors[current]
            if current is None:
                return []  # Tidak ada jalur
        
        path.append(start)
        path.reverse()
        return path
    
    # Mencari jalur terpendek dari 'A' ke 'D'
    distances, predecessors = dijkstra_with_path(graph, start_node)
    end_node = 'D'
    shortest_path = reconstruct_path(predecessors, start_node, end_node)
    
    print(f"\nJalur terpendek dari {start_node} ke {end_node}: {' -> '.join(shortest_path)}")
    print(f"Total jarak: {distances[end_node]}")