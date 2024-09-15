from math import gcd
from sys import stderr

def dbg(a):
    print(f'    {a}', file=stderr)

def is_all_same(c):
    assert len(c) >= 1
    ans = True
    for i in range(len(c)-1):
        ans = ans and (c[i] == c[i+1])
    return ans

def solve(c, d):
    ans = d
    for i in range(len(c)):
        c[i] %= d
    c.sort()
    if is_all_same(c):
        return 0
    for i in range(len(c)):
        ip = (i+1) % len(c)
        if c[i] == c[ip]:
            continue
        ans = min(ans, (c[i] - c[ip]) % d)
    return ans


T = int(input())

for t in range(T):
    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    d = gcd(a, b)
    print(solve(c,d))
