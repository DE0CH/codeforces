def count(ps):
    #partial sum
    existing = set()
    ans = 0
    for m in ps:
        if m in existing:
            ans += 1
            existing = set()
        existing.add(m)
    return ans

def cps(ar):
    # calculate partial sum
    ps = [0]
    for m in ar:
        ps.append(ps[-1] + m)
    return ps

def solution(ar):
    ps = cps(ar)
    return count(ps)

t = int(input())

for _ in range(t):
    input()
    ar = list(map(int, input().split()))
    print(solution(ar))

