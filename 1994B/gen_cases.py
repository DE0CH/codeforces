import random

# random.seed(42)
t = 1000
print(t)
for _ in range(t):
    n = random.randint(2, 10)
    # s = [i for i in range(1, n+1) for _ in range(2)]
    s = list(range(1, n+1)) + list(range(1, n+1))
    random.shuffle(s)
    k = random.randint(1, n//2)
    print(n, k)
    print(*s)
