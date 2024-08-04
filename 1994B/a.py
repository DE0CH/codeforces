# https://codeforces.com/problemset/problem/1994/B

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    t = input()
    
    solved = True
    for i in range(n):
        if s[i] == '1':
            break
        if s[i] == '0' and t[i] == '1':
            solved = False
            break
    print('Yes' if solved else 'No')

