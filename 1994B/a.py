t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a_two_times = set()
    a_one_time_t = set()
    a_one_time = set()
    b_two_times = set()
    b_one_time_t = set()
    s = list(map(int, input().split()))
    for i in range(n):
        if s[i] in a_one_time_t:
            a_two_times.add(s[i])
        else:
            a_one_time_t.add(s[i])
    for i in range(n):
        if s[i] not in a_two_times:
            a_one_time.add(s[i])
    
    for i in range(n, 2*n):
        if s[i] in b_one_time_t:
            b_two_times.add(s[i])
        else:
            b_one_time_t.add(s[i])
    # assert(a_one_time == b_one_time) # but this is too expensive so won't do this, but this is true
    a_one_time = list(a_one_time)
    m = len(a_two_times)
    a_two_times = list(a_two_times)
    b_two_times = list(b_two_times)
    # print(set(a_one_time).isdisjoint(set(a_two_times)))

    print(*(a_two_times[:k] + a_two_times[:k] + a_one_time[:max(2*k-2*m, 0)]))
    print(*(b_two_times[:k] + b_two_times[:k] + a_one_time[:max(2*k-2*m, 0)]))