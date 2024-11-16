t = int(input())

for _ in range(t):
    n = int(input())
    x = 0
    ans = 0
    i = 1
    while -n <= x <= n:
        if i % 2 == 0:
            x += 2 * i - 1
        else:
            x -= 2 * i - 1
        ans += 1
    if ans % 2 == 0:
        print('Kosuke')
    else:
        print('Sakurako')

    