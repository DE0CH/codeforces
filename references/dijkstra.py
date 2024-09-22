import heapq

MAXN = 200000

adj = [[] for _ in range(MAXN)]
d = [float('inf') for _ in range(MAXN)]
p = [-1 for _ in range(MAXN)]
queue = []

# Don't allocate d and p because it is too expensive for multiple test cases
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


n, m = map(int, input().split())
for i in range(n):
    adj[i].clear()

for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    adj[u].append((w, v))
    adj[v].append((w, u))

dijkstra(n, 0, d, p)

element = n-1
path = []
while element != 0 and element != -1:
    path.append(element)
    element = p[element]
if element == -1:
    print(-1)
else:
    print(1, *reversed([i + 1 for i in path]))