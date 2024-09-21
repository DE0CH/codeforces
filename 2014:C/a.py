from fractions import Fraction
from math import floor
from sys import stderr

def dbg(s):
    print(f'    {s}', file=stderr)

def round_up(a):
    return floor(a + 1)

def j(n):
    return n // 2

T = int(input())

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue
    if n == 2:
        print(-1)
        continue

    A.sort()
    a = Fraction(sum(A), n)
    b = 2 * A[j(n)]
    # dbg(f'{a} {b}')
    if a > b:
        print(0)
        continue
    print(round_up((b - a) * n))

