import heapq

def a_star(grid, start, goal):
    N, M = len(grid), len(grid[0])
    sx, sy = start
    gx, gy = goal

    def heuristic(x, y):
        return abs(x - gx) + abs(y - gy)

    visited = [[False]*M for _ in range(N)]
    heap = [(heuristic(sx, sy), 0, sx, sy)]  # (f, g, x, y)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        f, g, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True

        if (x, y) == (gx, gy):
            return g

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and grid[nx][ny] == 0:
                    heapq.heappush(heap, (g + 1 + heuristic(nx, ny), g + 1, nx, ny))
    return -1
# Input
def cekPath():
    N, M = map(int, input().split())
    sx, sy, gx, gy = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = a_star(grid, (sx, sy), (gx, gy))
    print(result)

cekPath()