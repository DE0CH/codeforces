T = int(input())
for _ in range(T):
    n, x = map(int, input().split())
    s1 = list(map(int, input().split()))
    v1 = 0
    s2 = list(map(int, input().split()))
    v2 = 0
    s3 = list(map(int, input().split()))
    v3 = 0
    b = 0
    while v1 < len(s1):
        if b == x:
            break
        c = s1[v1]
        if b | c | x == x:
            b = b | c
            v1 += 1
        else:
            break

    while v2 < len(s2):
        if b == x:
            break
        c = s2[v2]
        if b | c | x == x:
            b = b | c
            v2 += 1
        else:
            break

    while v3 < len(s3):
        if b == x:
            break
        c = s3[v3]
        if b | c | x == x:
            b = b | c
            v3 += 1
        else:
            break
    print("Yes" if b == x else "No")
