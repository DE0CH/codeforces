t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    if m == a[0]:
        print('Bob')
    else:
        print('Alice')

