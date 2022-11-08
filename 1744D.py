t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for j in a:
        while j % 2 == 0:
            j //=2
            ans += 1
    diff = max(0, n-ans)
    id = []
    for i in range(1, n +1):
        aa  = 0
        while i % 2 == 0:
            aa += 1
            i //=2
        id.append(aa)
    id.sort(reverse=True)
    ab = 0
    i = 0
    while diff > 0 and i < n:
        diff -= id[i]
        ab += 1
        i += 1
    if diff <= 0:
        print(ab)
    else:
        print(-1)

            