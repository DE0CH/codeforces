from sys import stderr
s = input()

def find_resulting_point(s):
    x = 0
    y = 0
    for m in s:
        if m == 'N':
            y += 1
        elif m == 'S':
            y -= 1
        elif m == 'E':
            x += 1
        elif m == 'W':
            x -= 1
    return x, y

# find out destination point

x, y = find_resulting_point(s)

if x % 2 != 0 or y % 2 != 0:
    print('NO')
# if same, addition check if a pair can be given
elif x == 0 and y == 0:
    axis = {'E': 0, 'W': 1, 'N': 0, 'S': 1}
    if len(s) <= 2:
        print('NO')
    else:
        chars = None
        for chars_cand in [{'N', 'S'}, {'E', 'W'}]:
            if set(s) >= chars_cand:
                chars = chars_cand
        assert chars is not None
    remaining = [1, 1]
    # print(chars, file=stderr)
    for m in s:
        # print(remaining, file=stderr)
        if m in chars and remaining[axis[m]] > 0:
            print('H', end='')
            remaining[axis[m]] -= 1
        else:
            print('R', end='')
    print()
elif x != 0 or y != 0:
    # print('not at origin', file=stderr)
    remaining = [abs(x // 2), abs(y // 2)]
    # print(remaining, file=stderr)
    axis = {'E': 0, 'W': 0, 'N': 1, 'S': 1}
    chars = set()
    if x > 0:
        chars.add('E')
    elif x < 0:
        chars.add('W')
    else:
        pass
    if y > 0:
        chars.add('N')
    elif y < 0:
        chars.add('S', 1)
    else:
        pass
    for m in s:
        if m in chars and remaining[axis[m]] > 0:
            print('H', end='')
            remaining[axis[m]] -= 1
        else:
            print('R', end='')
    print()
else:
    raise ValueError('Condition is not exhaustive')
# if not same, greedy
# find out if destination point is same as landing point

# give the pairs