from math import sqrt

def increment(counter, max_things):
    assert len(counter) == len(max_things)
    for i in range(len(counter)):
        counter[i] += 1
        if counter[i] <= max_things[i]:
            break
        elif counter[i] == max_things[i] + 1:
            counter[i] = 0
        else:
            raise ValueError("impossible counter count")

def prime_factors(a, b):
    numbers = [0]
    factors = [0]
    j = 0
    ap = a
    bp = b
    a = min(ap, bp)
    b = max(ap, bp)
    i = 2
    bo = b
    while i <= sqrt(bo):
        if a % i == 0 or b % i == 0:
            if a % i == 0:
                a //= i
            elif b % i == 0:
                b //= i
            else:
                raise ValueError("impossible condition") 
            if i != factors[j]:
                j += 1
                numbers.append(0)
                factors.append(i)
            numbers[j] += 1
        else:
            i += 1

    if a == b and a != 1:
        numbers.append(2)
        factors.append(a)
        a = 1
        b = 1
    if a != 1:
        numbers.append(1)
        factors.append(a)
        a = 1
    if b != 1:
        numbers.append(1)
        factors.append(b)
        b = 1

    return numbers[1:], factors[1:]

def get_number(counter, factors):
    ans = 1
    assert len(counter) == len(factors)
    for i in range(len(counter)):
        ans *= factors[i] ** counter[i]
    return ans


t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())

    numbers, factors = prime_factors(a, b)
    
    counter = [0 for i in range(len(factors))]

    stop = False
    k = 1
    ya = -1
    xa = -1
    while not stop:
        x = c // k * k
        s = a * b // k
        y = d // s * s
        if a < x and b < y:
            xa = x
            ya = y
            break
        increment(counter, numbers)
        k = get_number(counter, factors)
        if k == 1:
            stop = True
    print(xa, ya)

