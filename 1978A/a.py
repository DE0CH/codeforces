def solve(books):
    max = 0
    for i in range(len(books) - 2, -1, -1):
        if books[i] > max:
            max = books[i]
    return max + books[-1]


tc = int(input())


for t in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))