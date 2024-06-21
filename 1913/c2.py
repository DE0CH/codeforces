db = [0 for i in range(30)]

def insert(x):
    db[x] += 1

def query(y):
    for i in reversed(range(30)):
        y -= 2**i * min(db[i], y // 2**i)
    return y == 0

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if a == 1:
        insert(b)
    else:
        print('YES' if query(b) else 'NO')
