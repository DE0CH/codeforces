from sys import stderr
import heapq

MAXN = 200000

adj = [[] for _ in range(2*MAXN)]
s1 = [float('inf') for _ in range(2*MAXN)]
s2 = [float('inf') for _ in range(2*MAXN)]
p = [-1 for _ in range(2*MAXN)]
queue = []


def dijkstra(n, s, d, p):
    d.clear()
    p.clear()
    queue.clear()
    for i in range(n):
        d.append(float('inf'))
        p.append(-1)
    d[s] = 0
    heapq.heappush(queue, (0, s))
    while True:
        try:
            d_v, v = heapq.heappop(queue)
        except IndexError:
            break
        if d_v != d[v]:
            continue
        for len, to in adj[v]:
            if (d[v] + len < d[to]):
                d[to] = d[v] + len
                p[to] = v
                heapq.heappush(queue, (d[to], to))

T = int(input())

for _ in range(T):
    n, m, h = map(int, input().split())
    for i in range(2*n):
        adj[i].clear()
    for i in map(int, input().split()):
        i -= 1
        adj[i].append((0, i+n))
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((w, v))
        adj[v].append((w, u))
        adj[u+n].append((w//2, v+n))
        adj[v+n].append((w//2, u+n))
    dijkstra(n*2, 0, s1, p)
    dijkstra(n*2, n-1, s2, p)
    ans = float('inf')
    for i in range(n):
        ans = min(ans, max(min(s1[i], s1[i+n]), min(s2[i], s2[i+n])))
    if ans < float('inf'):
        print(ans)
    else:
        print(-1)