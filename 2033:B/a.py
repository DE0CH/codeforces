
# matrix with diagonal starting at (i, 0)
def min_diagonal(i, m, n):
    minn = 0
    for j in range(n):
        minn = min(m[i+j][j], minn)
    return minn

def solution(m, n):
    # add another matrix of m on the right
    new_m = [[0 for _ in range(n)] for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_m[i+n][j] = m[i][j]
    maxx = 0
    for i in range(2*n):
        
        maxx += -min_diagonal(i, new_m, n)
    return maxx

t = int(input())

for _ in range(t):
    n = int(input())
    m = []
    for i in range(n):
        m.append(list(map(int, input().split())))
    print(solution(m, n))