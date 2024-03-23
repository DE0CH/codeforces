from decimal import Decimal
from sys import stderr

t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    x *= 100
    y *= 100
    savings = 0
    for __ in range(n):
        s = input()[:-1]
        v = round(float(s) * 100)
        s = v % y
        if s != 0:
            savings += y - s
    if savings >= x:
        print('YES')
    else:
        print('NO')