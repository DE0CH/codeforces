T = int(input())

for _ in range(T):
    _, k = map(int, input().split())
    A = list(map(int, input().split()))
    robin = 0
    ans = 0
    for a in A:
        if a >= k:
            robin += a
        elif a == 0 and robin > 0:
            robin -= 1
            ans += 1
    print(ans)

        
