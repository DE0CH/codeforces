from sys import stderr

T = int(input())

for _ in range(T):
    n, d, k = map(int, input().split())
    J = [0 for _ in range(n - d + 1)]
    for _ in range(k):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        J[max(l - d + 1, 0)] += 1
        if r + 1 <= n-d:
            J[r + 1] -= 1
    # print(J, file=stderr)
    moving_sum = 0
    minn = k + 1
    maxx = -1
    min_i = -1
    max_i = -1
    for (i, a) in enumerate(J):
        moving_sum += a
        if moving_sum > maxx:
            maxx = moving_sum
            max_i = i
        if moving_sum < minn:
            minn = moving_sum
            min_i = i
    print(max_i+1, min_i+1)
    