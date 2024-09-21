from sys import stderr
import heapq

def dijkstra(vertex, edges, start):
    queue = []
    dist = [float('inf') for _ in vertex]
    dist[start] = 0
    heapq.heappush(queue, (0, start))
    while True:
        try:
            d, u = heapq.heappop(queue)
        except IndexError:
            break
        for w, v in edges[u]:
            alt = dist[u] + w
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(queue, (alt, v))
    return dist

def solve(vertex, edges, horses, start):
    new_vertex = range(len(vertex) * 2)
    new_edges = [[] for _ in new_vertex]
    for i in vertex:
        new_edges[i] = [(w, u) for w, u in edges[i]]
        new_edges[i + len(vertex)] = [(w // 2, u + len(vertex)) for w, u in edges[i]]
        if horses[i]:
            new_edges[i].append((0, i + len(vertex)))
    s = dijkstra(new_vertex, new_edges, start)
    ans = [0 for _ in vertex]
    for i in vertex:
        ans[i] = min(s[i], s[i + len(vertex)])
    return ans


T = int(input())

for _ in range(T):
    n, m, h = map(int, input().split())
    horses_index = [int(s) - 1 for s in input().split()]
    horses = [False for _ in range(n)]
    for i in horses_index:
        horses[i] = True
    vertex = range(n)
    edges = [[] for _ in vertex]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append((w, v))
        edges[v].append((w, u))
    s1 = solve(vertex, edges, horses, 0)
    s2 = solve(vertex, edges, horses, n - 1)
    ans = float('inf')
    for i in range(n):
        ans = min(ans, max(s1[i], s2[i]))
    if ans < float('inf'):
        print(ans)
    else:
        print(-1)