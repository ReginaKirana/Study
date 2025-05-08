import sys

def mau_pulang(N, adj):
    result = []
    
    def dfs(u, target, visited):
        if visited[u]:
            return False
        visited[u] = True
        if u == target:
            return True
        for w in adj[u]:
            if dfs(w, target, visited):
                return True
        return False

    for i in range(1, N+1):
        found = False
        for v in adj[i]:
            visited = [False] * (N+1)
            if dfs(v, i, visited):
                found = True
                break
        if found:
            result.append(i)
    return result

def tes_mau_pulang():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    adj = [[] for i in range(N+1)]
    for j in range(M):
        A, B = map(int, input().split())
        adj[A].append(B)

    hasil = mau_pulang(N, adj)
    if not hasil:
        print(-1)
    else:
        print(*hasil)

tes_mau_pulang()