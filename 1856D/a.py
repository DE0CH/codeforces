import sys

def ask(l, r):
    if l+1 == r:
        return 0
    print(f'? {l+1} {r}')
    sys.stdout.flush()
    a = int(input())
    if a == -1:
        raise RuntimeError('-1 given')
    return a

def largest(l, r):
    if l+1 == r:
        return l
    if l+2 == r:
        return l+1 if ask(l, r) == 0 else l
    m = (l+r) // 2
    lg = largest(l, m)
    rg = largest(m, r)
    return rg if ask(lg, rg) == ask(lg, rg+1) else lg

t = int(input())
for _ in range(t):
    n = int(input())
    g = largest(0, n)
    print(f'! {g+1}')
    sys.stdout.flush()
