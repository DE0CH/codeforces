mod = 10**9+7

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
    
def pow(a, i, m):
    return modinv(a, m)

def factorial_change(n, m):
    if n == m:
        return 1
    if m > n:
        ans = 1
        for i in range(n+1, m+1):
            ans = (ans * i) % mod
    if m < n:
        ans = 1
        for i in range(m+1, n+1):
            ans = (ans * pow(i, -1, mod)) % mod
    return ans

def comb_change(n1, k1, n2, k2):
    ans = 1
    ans = (ans * factorial_change(n1, n2)) % mod
    ans = (ans * factorial_change(k2, k1)) % mod
    ans = (ans * factorial_change(n2 - k2, n1 - k1)) % mod
    return ans

def cc(prev, n2, k2):
    ans = prev[0]
    n1, k1 = prev[1:3]
    return ((ans * comb_change(n1, k1, n2, k2)) % mod, n2, k2)

def solution(n):
    ans = 0
    one_prev = (1, 0, 0)
    two_prev = (1, 0, 0)
    three_prev = (1, 0, 0)
    four_prev = (1, 0, 0)
    five_prev = (1, 0, 0)
    abs_a = n
    for abs_b in range(0, n+1):
        if abs_a <= abs_b * 2:
            one = cc(one_prev, abs_a, abs_b)
            ans = (ans + (abs_b * 2 + 1) * one[0]) % mod
            one_prev = one
        else:
            for mex in range(abs_b + 1, 2*abs_b + 2):
                if mex == abs_b + 1:
                    two = cc(four_prev, mex-1, abs_b)
                    four_prev = two
                    three = cc(five_prev, abs_a - mex, 2 * abs_b + 1 - mex)
                    five_prev = three
                else:
                    two = cc(two_prev, mex-1, abs_b)
                    three = cc(three_prev, abs_a - mex, 2 * abs_b + 1 - mex)
                two_prev = two
                three_prev = three
                ans = (ans + (mex*two[0]*three[0])) % mod

    return ans

t = int(input())

for _ in range(t):
    n = int(input())
    print(solution(n))
