# from sys import stderr
t = int(input())

G = dict()
for _ in range(t):
    a, b = input().split()
    if a not in G:
        G[a] = dict()
    if b not in G[a]:
        G[a][b] = 0
    G[a][b] += 1

# print(G, file=stderr)
ans = 0
for a in G:
    required = max(G[a].values())
    ans += required

print(ans)