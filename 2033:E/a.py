def find_cycle(i, ar, visited):
    # find cycle to swap in ar, the first element being i, return the cycle length and modify visited
    cycle = [i]
    starting = i
    visited[i] = True
    current = ar[i]
    while current != starting:
        cycle.append(current)
        visited[current] = True
        current = ar[current]
    ans = len(cycle) - 1 - len(cycle) // 2

    return ans


def sort(ar):
    visited = [False for _ in range(len(ar))]
    ans = 0
    i = 0
    while i < len(ar):
        ans += find_cycle(i, ar, visited)
        while i < len(ar) and visited[i] :
            i += 1
    return ans

t = int(input())

for _ in range(t):
    input()
    ar = list(map(int, input().split()))
    ar = [i-1 for i in ar]
    print(sort(ar))