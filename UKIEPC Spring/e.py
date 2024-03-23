def passes(time):
    if time == 0:
        return 0
    return (time-1) // 720 + 1

t = int(input())
for _ in range(t):
    T, d = map(int, input().split())
    T *= 11
    d *= 11
    ans = (T+d+1) // (720 * 11) * 11
    ans -= passes(T)
    ans += passes((T+d+1) % (720 * 11)) 

    print(ans)