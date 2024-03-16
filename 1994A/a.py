t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(n if k < n-1 else 1)