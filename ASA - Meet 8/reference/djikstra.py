import heapq

def dijkstra(graph, start):
    # graph: dict {node: [(neighbor: weight),....]}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# Contoh penggunaan
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'A': 4, 'F': 5, 'E': 12},
    'C': {'A':3,'D':7,'E':10},
    'D': {'C': 7, 'E': 2},
    'E': {'C':10,'D':2, 'Z':5},
    'F': {'B':4,'Z':16},
    'Z': {'E':5,'F':16}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print("Jarak terpendek dari node", start_node)
for node, distance in distances.items():
    print("Ke node", node, ":", distance)