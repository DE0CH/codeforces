def make_f(a):
    def f(i, y):
        if i == len(a)-1 and a[i] < y:
            return float('inf')
        if a[i] >= y:
            return 0
        if a[i] < y:
            return y - a[i] + f(i+1, y-1)
    return f

def make_g(a):
    f = make_f(a)
    def g(y):
        k = float('inf')
        for i in range(len(a)):
            k = min(k, f(i, y))
        return k
    return g

def bs(g, l, r, k):
    if l == r-1:
        return l
    m = (l+r) // 2
    if g(m) <= k:
        return bs(g, m, r, k)
    else:
        return bs(g, l, m, k)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    g = make_g(a)
    print(bs(g, max(*a), max(*a) + n, k))
