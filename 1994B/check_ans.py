from multiset import Multiset
t = int(input())
cases = []
for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    cases.append((n, k, s))
for i in range(0, t):
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    n, k, s = cases[i]
    print(i)
    assert Multiset(s[:n]) >= Multiset(l)
    assert Multiset(s[n:2*n]) >= Multiset(r)
    assert len(l) == 2*k
    assert len(r) == 2*k

    xor_ans = 0
    xor_ans_2 = 0
    for x in l:
        xor_ans ^= x
    for x in r:
        xor_ans_2 ^= x
    assert xor_ans == xor_ans_2

