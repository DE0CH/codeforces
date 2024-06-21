t = int(input())
for _ in range(t):
    count = [0, 0]
    s = input().strip()
    for c in s:
        count[int(c)] += 1
    diff = count[0] - count[1]
    if diff == 0:
        print(0)
        continue
    ans = 0
    active = diff < 0
    diff = abs(diff)
    for i in reversed(range(0, len(s))):
        if int(active) == int(s[i]):
            diff -= 1
        ans += 1
        if diff == 0:
            print(ans)
            break
