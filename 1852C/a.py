fm = [[None, None] for _ in range(200000)]
def f(a, k, n, extend):
    if n < 1:
        raise ValueError('n must be greater than 1')
    if n == 1 and extend == 1:
        res = (a[0], a[0])
    elif n == 1 and extend == 0:
        res = (0, float('inf'))
    else:
        diff = (a[n-1] - a[n-2]) % k
        if fm[n][extend] is not None:
            return fm[n][extend]
        if f(a, k, n-1, 0)[0] + diff < k:
            prev = f(a, k, n-1, 1)
        else:
            prev = min(f(a, k, n-1, 0), f(a, k, n-1, 1), key=lambda x: x[1])
        if extend:
            res = (prev[0] + diff, prev[1] + diff)
        else:
            height = prev[0] + diff - k
            stroke = prev[1]
            if height < 0:
                res = (0, float('inf'))
            else:
                res = (height, stroke)
    fm[n][extend] = res
    return res

def main():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        a = list(map(lambda x: x % k, a)) # pylint: disable=cell-var-from-loop
        print(a)
        print(min(f(a, k, n, 0)[1], f(a, k, n, 1)[1]))
        print(fm[:n+1])
        for i in range(n):
            fm[i+1][0] = None
            fm[i+1][1] = None

if __name__ == '__main__':
    main()
