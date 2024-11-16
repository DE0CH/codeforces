def try_remove(ll, c):
    try:
        ll.remove(c)
    except ValueError:
        pass

def sp(c1, c2):
    ans1 = [c1[0]]
    ans2 = [c2[0]]
    assert len(c1) == len(c2)
    n = len(c1)
    for i in range(1, n):
        choices = [0, 1]
        if ans1[i-1] == c1[i] and ans1[i-1] != c2[i]:
            try_remove(choices, 0)
        elif ans1[i-1] == c2[i] and ans1[i-1] != c1[i]:
            try_remove(choices, 1)
        if ans2[i-1] == c1[i] and ans2[i-1] != c2[i]:
            try_remove(choices, 1)
        elif ans2[i-1] == c2[i] and ans2[i-1] != c1[i]:
            try_remove(choices, 0)
        if len(choices) > 0:
            if choices[0] == 0:
                ans1.append(c1[i])
                ans2.append(c2[i])
            else:
                ans1.append(c2[i])
                ans2.append(c1[i])
        else:
            ans1.append(c1[i])
            ans2.append(c2[i])
    return ans1, ans2
def count_dist(a):
    n = len(a)
    ans = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            ans += 1
    return ans

def solution(m):
    n = len(m)
    if n % 2 == 0:
        half_n = n // 2
    else:
        half_n = n // 2 + 1
    c1 = []
    c2 = []
    for i in range(half_n):
        c1.append(m[i])
        c2.append(m[n-1-i])
    ans1, ans2 = sp(c1, c2)
    ans = []
    for i in range(half_n):
        ans.append(ans1[i])
    for i in range(half_n):
        ans.append(ans2[half_n - 1 - i])
    cc = count_dist(ans)
    cc -= (n % 2)
    return cc

t = int(input())

for _ in range(t):
    input()
    m = list(map(int, input().split()))
    print(solution(m))
