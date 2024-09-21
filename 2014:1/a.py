from sys import stderr

def dbg(s):
    print(f'    {s}', file=stderr)
def solve(n, even):
    # dbg(f'{n} {even}')
    # 0 means even, 1 means odd
    remainder = n % 4
    if remainder == 1 and even:
        return 0
    elif remainder == 1 and not even:
        return 1
    elif remainder == 2:
        return 1
    elif remainder == 3 and even:
        return 1
    elif remainder == 3 and not even:
        return 0
    elif remainder == 0:
        return 0
    else:
        raise RuntimeError("condition is not exhaustive")

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    if solve(min(n, k), bool(n % 2 == 0)) == 0:
        print('YES')
    else:
        print('NO')
