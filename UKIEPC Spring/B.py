t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    if x == 0 or y == 0 or z >= 1:
        print('YES')
    else:
        print('NO')