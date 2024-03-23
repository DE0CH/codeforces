# from sys import stderr
t = int(input())

def distance(ax, ay, bx, by):
    # Euclidean distance squared
    return (ax - bx) ** 2 + (ay - by) ** 2

for _ in range(t):
    ax, ay, bx, by, gx, gy, s, k = map(int, input().split())
    # if same distance is draw
    if distance(ax, ay, gx, gy) == distance(bx, by, gx, gy):
        # print('equal distance', file=stderr)
        print('Draw')
    # else if both cannot reach in time, it is a draw
    elif distance(ax, ay, gx, gy) > (s * k) ** 2 and distance(bx, by, gx, gy) > (s * k) ** 2:
        print('Draw')
    # else (implying one of them can reach in time and they don't reach at the same time) the closest one wins 
    elif distance(ax, ay, gx, gy) < distance(bx, by, gx, gy):
        print('Alice')
    elif distance(ax, ay, gx, gy) > distance(bx, by, gx, gy):
        print('Bob')
    else:
        raise ValueError('Condition is not exhaustive')