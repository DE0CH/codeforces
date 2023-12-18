import subprocess

n = int(input())
a = list(map(int, input().split()))

def q(l, r):
    inversions = 0
    for i in range(l, r):
        for j in range(i+1, r):
            if a[i] > a[j]:
                print(i, j)
                inversions += 1
    return inversions

def ans():
    max = 0
    max_i = -1
    for i in range(0, n):
        if a[i] > max:
            max = a[i]
            max_i = i
    return max_i

p = subprocess.Popen(['python3', 'a.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
p.stdin.write('1\n'.encode())
p.stdin.flush()
p.stdin.write(str(n).encode())
p.stdin.write('\n'.encode())
p.stdin.flush()
out = p.stdout.readline().decode().strip()
while out.startswith('?'):
    print(out)
    l, r = map(int, out.split()[1:])
    l -= 1
    w = f'{q(l, r)}\n'
    print(f'q(l, r): {w}', end='')
    p.stdin.write(w.encode())
    p.stdin.flush()
    out = p.stdout.readline().decode().strip()
print(out)
if out.startswith('!'):
    candidate = int(out.split()[1]) - 1
    if candidate == ans():
        print('yes')
    else:
        print('no')
        print(ans())
else:
    print('wrong format')
