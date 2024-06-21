def is_valid(a, b):
    return a[0] != '0' \
        and b[0] != '0' \
        and int(a) < int(b) \
        and int(a) > 0

t = int(input())
for _ in range(t):
    c = input().strip()
    found = False
    for i in range(1, len(c)):
        a = c[:i]
        b = c[i:]
        if is_valid(a, b):
            print(a, b)
            found = True
            break
    if not found: print('-1')
