import heapq

def dijkstra(n, s, adj):
    d = []
    p = []
    queue = []
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
    return (d, p)

# https://codeforces.com/problemset/problem/20/C

n, m = map(int, input().split())
adj = [[] for _ in range(n)]

for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((w, v))
    adj[v].append((w, u))

d, p = dijkstra(n, 0, adj)

element = n-1
path = []
while element != 0 and element != -1:
    path.append(element)
    element = p[element]
if element == -1:
    print(-1)
else:
    print(1, *reversed([i + 1 for i in path]))